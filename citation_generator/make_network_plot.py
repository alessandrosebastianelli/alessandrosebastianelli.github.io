import re
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch
import numpy as np


def normalize_author_name(name):
    """
    Normalize author names to handle abbreviations and variations.
    Returns (last_name, first_initial) tuple for matching.
    """
    # Remove extra whitespace
    name = ' '.join(name.split())
    
    # Remove periods and special characters
    name = name.replace('.', '').replace('{', '').replace('}', '').replace('\\', '').replace('~', '')
    
    # Handle special cases like "Del Rosso" or "Le Saux"
    # These compound last names should be treated as a unit
    name_lower = name.lower()
    
    # Split by comma first (format: Last, First)
    if ',' in name:
        parts = name.split(',')
        last_name = parts[0].strip()
        first_part = parts[1].strip() if len(parts) > 1 else ''
    else:
        # Split by space (format: First Last or F Last)
        parts = name.split()
        if len(parts) >= 2:
            # Handle compound last names (del, de, le, van, von, di, etc.)
            compound_prefixes = ['del', 'de', 'le', 'van', 'von', 'di', 'da', 'dos', 'las']
            
            # Find where the last name starts
            last_name_parts = []
            first_name_parts = []
            found_prefix = False
            
            for i, part in enumerate(parts):
                if part.lower() in compound_prefixes or found_prefix:
                    last_name_parts.append(part)
                    found_prefix = True
                elif i == len(parts) - 1:  # Last element is always part of last name
                    last_name_parts.append(part)
                else:
                    first_name_parts.append(part)
            
            last_name = ' '.join(last_name_parts)
            first_part = ' '.join(first_name_parts)
        else:
            last_name = name.strip()
            first_part = ''
    
    # Clean last name
    last_name = last_name.strip().lower()
    
    # Get first initial (can be multiple initials like "MP")
    first_part = first_part.strip()
    if first_part:
        # Remove spaces between initials: "M P" -> "MP"
        first_initials = ''.join([c for c in first_part if c.isalpha()])[:2].lower()
    else:
        first_initials = ''
    
    return (last_name, first_initials)


def names_match(name1, name2):
    """Check if two names refer to the same person."""
    n1 = normalize_author_name(name1)
    n2 = normalize_author_name(name2)
    
    # Exact match
    if n1 == n2:
        return True
    
    # Same last name and first initial matches (if both have initials)
    if n1[0] == n2[0]:
        if n1[1] and n2[1]:
            # At least one initial must match
            if n1[1][0] == n2[1][0]:
                return True
    
    return False


def get_full_name(name):
    """Get a clean full name for display."""
    name = ' '.join(name.split())
    name = name.replace('.', '')
    
    # Handle "Last, First" format
    if ',' in name:
        parts = name.split(',')
        last = parts[0].strip()
        first = parts[1].strip() if len(parts) > 1 else ''
        return f"{last}, {first}" if first else last
    
    return name


def parse_bibtex_authors(filepath):
    """Parse BibTeX file and extract co-authorship information including co-author connections."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split entries
    entries = re.split(r'\n\s*@', content)
    entries = ['@' + entry if not entry.startswith('@') else entry for entry in entries if entry.strip()]
    
    # Track collaborations with full names as keys
    author_collaborations = defaultdict(int)
    coauthor_connections = defaultdict(int)  # Track connections between co-authors
    seen_normalized = {}  # Map normalized tuples to chosen display name
    
    target_normalized = normalize_author_name("Alessandro Sebastianelli")
    
    for entry in entries:
        # Extract authors
        author_match = re.search(r'author\s*=\s*\{([^}]+)\}', entry)
        if not author_match:
            author_match = re.search(r'author\s*=\s*([^,]+),', entry)
        
        if not author_match:
            continue
        
        authors_str = author_match.group(1)
        
        # Split by 'and' or semicolon
        authors = re.split(r'\s+and\s+|;\s*', authors_str)
        
        # Process authors
        has_target = False
        paper_authors = []
        
        for author in authors:
            author = author.strip()
            if not author:
                continue
            
            normalized = normalize_author_name(author)
            full_name = get_full_name(author)
            
            # Choose display name - prefer longer, more complete names
            if normalized in seen_normalized:
                display_name = seen_normalized[normalized]
                # Update if we find a longer name
                if len(full_name) > len(display_name):
                    # Update all existing references
                    old_count = author_collaborations.get(display_name, 0)
                    if old_count > 0:
                        del author_collaborations[display_name]
                        author_collaborations[full_name] = old_count
                    seen_normalized[normalized] = full_name
                    display_name = full_name
            else:
                display_name = full_name
                seen_normalized[normalized] = display_name
            
            paper_authors.append(display_name)
            
            # Check if this is Alessandro Sebastianelli
            if normalized == target_normalized:
                has_target = True
        
        # If Alessandro is in this paper, count collaborations with others
        if has_target:
            non_alessandro_authors = []
            for display_name in paper_authors:
                # Check if this is Alessandro
                author_norm = normalize_author_name(display_name)
                if author_norm != target_normalized:
                    author_collaborations[display_name] += 1
                    non_alessandro_authors.append(display_name)
            
            # Count co-author connections (between non-Alessandro authors on same paper)
            for i, author1 in enumerate(non_alessandro_authors):
                for author2 in non_alessandro_authors[i+1:]:
                    # Create ordered pair for consistent key
                    pair = tuple(sorted([author1, author2]))
                    coauthor_connections[pair] += 1
    
    return author_collaborations, coauthor_connections, target_normalized


def create_collaboration_network(bib_file, output_file):
    """Create a network visualization of co-authors."""
    print("Parsing BibTeX file for co-authors...")
    collaborations, coauthor_connections, target = parse_bibtex_authors(bib_file)
    
    if not collaborations:
        print("No collaborations found!")
        return
    
    print(f"Found {len(collaborations)} unique co-authors (after consolidation)")
    print(f"Found {len(coauthor_connections)} co-author connections")
    
    # Create graph
    G = nx.Graph()
    
    # Add central node (Alessandro)
    target_name = "Sebastianelli, Alessandro"
    G.add_node(target_name, node_type='center', papers=sum(collaborations.values()))
    
    # Add co-author nodes and edges to Alessandro
    for coauthor_name, count in collaborations.items():
        G.add_node(coauthor_name, node_type='coauthor', papers=count)
        G.add_edge(target_name, coauthor_name, weight=count, edge_type='alessandro')
    
    # Add edges between co-authors
    for (author1, author2), count in coauthor_connections.items():
        if author1 in G.nodes and author2 in G.nodes:
            G.add_edge(author1, author2, weight=count, edge_type='coauthor')
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(22, 18), facecolor='white')
    ax.set_facecolor('white')
    
    # Use spring layout for more compact clustering (like reference image)
    # Adjust k parameter to control spacing - smaller k = tighter clustering
    pos = nx.spring_layout(G, k=0.8, iterations=100, seed=42)
    
    # Ensure Alessandro is near the center
    alessandro_pos = pos[target_name]
    center_offset = np.array([0, 0]) - alessandro_pos
    for node in pos:
        pos[node] = pos[node] + center_offset
    
    # Separate nodes
    center_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'center']
    coauthor_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'coauthor']
    
    # Node sizes based on number of papers - INCREASED SIZES
    center_size = [5000]  # Fixed size for Alessandro (not shown)
    coauthor_sizes = [max(600, G.nodes[n]['papers'] * 400) for n in coauthor_nodes]  # Doubled from 300/200
    
    # Assign unique colors to each co-author
    num_authors = len(coauthor_nodes)
    # Use a colormap with good distinction
    cmap = plt.cm.get_cmap('tab20')  # Up to 20 distinct colors, cycle if more
    author_colors = {}
    for i, author in enumerate(coauthor_nodes):
        author_colors[author] = cmap(i % 20)
    
    # Draw edges separately: Alessandro connections vs co-author connections
    alessandro_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('edge_type') == 'alessandro']
    coauthor_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('edge_type') == 'coauthor']
    
    # Draw co-author interconnections (thinner, gray)
    if coauthor_edges:
        coauthor_weights = [G[u][v]['weight'] for u, v in coauthor_edges]
        max_coauthor_weight = max(coauthor_weights) if coauthor_weights else 1
        
        for (u, v), weight in zip(coauthor_edges, coauthor_weights):
            alpha = 0.2 + (weight / max_coauthor_weight) * 0.3
            edge_width = 0.5 + (weight / max_coauthor_weight) * 1.5
            
            nx.draw_networkx_edges(
                G, pos, [(u, v)], 
                width=edge_width,
                alpha=alpha, 
                edge_color='gray',
                connectionstyle='arc3,rad=0.1',
                arrows=True,
                arrowstyle='-',
                ax=ax
            )
    
    # Draw Alessandro connections (colored, thicker)
    if alessandro_edges:
        alessandro_weights = [G[u][v]['weight'] for u, v in alessandro_edges]
        max_weight = max(alessandro_weights) if alessandro_weights else 1
        
        for (u, v), weight in zip(alessandro_edges, alessandro_weights):
            # Calculate edge properties
            alpha = 0.3 + (weight / max_weight) * 0.5
            edge_width = 0.5 + (weight / max_weight) * 3
            
            # Color based on weight
            color_intensity = weight / max_weight
            if color_intensity > 0.7:
                color = plt.cm.Greens(0.4 + color_intensity * 0.3)
            elif color_intensity > 0.4:
                color = plt.cm.YlOrBr(0.3 + color_intensity * 0.3)
            elif color_intensity > 0.2:
                color = plt.cm.RdPu(0.3 + color_intensity * 0.3)
            else:
                color = plt.cm.Blues(0.3 + color_intensity * 0.3)
            
            nx.draw_networkx_edges(
                G, pos, [(u, v)], 
                width=edge_width,
                alpha=alpha, 
                edge_color=[color],
                connectionstyle='arc3,rad=0.1',
                arrows=True,
                arrowstyle='-',
                ax=ax
            )
    
    # Don't draw center node (Alessandro) - keep invisible as connection point only
    
    # Draw co-author nodes with unique colors for each author
    for i, author in enumerate(coauthor_nodes):
        nx.draw_networkx_nodes(
            G, pos, 
            nodelist=[author],
            node_size=[coauthor_sizes[i]], 
            node_color=[author_colors[author]],
            node_shape='o', 
            alpha=0.85, 
            edgecolors='black',
            linewidths=1.5,
            ax=ax
        )
    
    # Draw labels with black font
    # Don't draw center label since center node is invisible
    
    # Co-author labels - black font - LARGER SIZE
    coauthor_labels = {n: n for n in coauthor_nodes}
    nx.draw_networkx_labels(
        G, pos, coauthor_labels, 
        font_size=11,  # Increased from 8
        font_weight='normal',
        font_color='black',
        font_family='sans-serif',
        ax=ax
    )
    
    # Add title - LARGER SIZE
    plt.title("Collaboration Network - Alessandro Sebastianelli", 
             fontsize=26, fontweight='bold', pad=20)  # Increased from 20
    
    # Add legend for node size - LARGER SIZES and BIGGER CIRCLES
    legend_sizes = [1, 3, 5, 10]
    legend_elements = []
    for size in legend_sizes:
        legend_elements.append(
            plt.Line2D([0], [0], marker='o', color='w', 
                      markerfacecolor='orange', markersize=np.sqrt(size*400/10),  # Scale properly
                      markeredgecolor='black', markeredgewidth=1.5,
                      label=f'{size} paper{"s" if size > 1 else ""}', linestyle='None')
        )
    
    legend = ax.legend(handles=legend_elements, loc='upper right', fontsize=14,  # Increased from 11
                      title='Collaboration Count', title_fontsize=16,  # Increased from 12
                      frameon=True, fancybox=True, shadow=True)
    # Make legend frame larger
    legend.get_frame().set_linewidth(2)
    legend.get_frame().set_edgecolor('black')
    
    # Remove title (cleaner look like reference)
    # Just keep it minimal
    
    # Add subtle text box with statistics in corner
    total_coauthors = len(coauthor_nodes)
    total_collaborations = sum(collaborations.values())
    
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    
    # Save figure
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Network visualization saved to: {output_file}")
    
    # Also save a list of top collaborators
    print("\nTop 10 Collaborators:")
    sorted_collabs = sorted(collaborations.items(), key=lambda x: x[1], reverse=True)
    for i, (name, count) in enumerate(sorted_collabs[:10], 1):
        print(f"{i}. {name}: {count} papers")
    
    plt.close()

if __name__ == '__main__':
    BIB_FILE = 'citation_generator/works.bib'
    OUTPUT_FILE = 'images/collaborations.png'
    
    create_collaboration_network(BIB_FILE, OUTPUT_FILE)
    print("\nDone!")