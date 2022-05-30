const c = 30;
const G = 2;
const dt = 0.1;
const yoff = 80;
let m87;

const particles = [];
let start, end;

function setup() {
  createCanvas(windowWidth, windowHeight);
  m87 = new Blackhole(width / 2, yoff+height / 2, 6500);

  start = yoff + height / 2;
  end = yoff + height / 2 - m87.rs * 2.6;

  for (let y = 0; y < start; y += 10) {
    particles.push(new Photon(width - 20, y));
  }
}

function draw() {
  background(255);

  stroke(0);
  strokeWeight(1);
  line(0, start, width, start);
  line(0, end, width, end);

  for (let p of particles) {
    m87.pull(p);
    p.update();
    p.show();
  }
  m87.show();

  push();
  fill(0);
  noStroke();
  textSize(16);
  textAlign(CENTER);
  textStyle(BOLD);
  text("Black Hole Visualization (by Daniel Shiffman)", 20*width/100, 58*height/100);
  pop();
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}