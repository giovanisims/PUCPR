let shoulderAngle = 0;
let elbowAngle = 0;
let wristAngle = 0;

const shoulderSpeed = 0.05;
const elbowSpeed = 0.05;
const wristSpeed = 0.05;

const armLength1 = 100;
const armLength2 = 80;
const handLength = 40;

function setup() {
  createCanvas(600, 400);
  angleMode(RADIANS);
}

function draw() {
  background(220);

  // Controles
  if (keyIsDown(81)) { // Q
    shoulderAngle -= shoulderSpeed;
  }
  if (keyIsDown(69)) { // E
    shoulderAngle += shoulderSpeed;
  }
  if (keyIsDown(65)) { // A
    elbowAngle -= elbowSpeed;
  }
  if (keyIsDown(68)) { // D
    elbowAngle += elbowSpeed;
  }
  if (keyIsDown(90)) { // Z
    wristAngle -= wristSpeed;
  }
  if (keyIsDown(67)) { // C
    wristAngle += wristSpeed;
  }

  // Corpo do robô
  translate(width / 2, height - 50); // Posiciona o robô na parte inferior central
  fill(100);
  rectMode(CENTER);
  rect(0, -25, 50, 100); // Corpo

  // Braço
  push();
  translate(0, -70); // Ponto de articulação do ombro no corpo

  // Ombro
  rotate(shoulderAngle);
  fill(150);
  rect(armLength1 / 2, 0, armLength1, 20); // Primeiro segmento do braço

  // Cotovelo
  translate(armLength1, 0); // Move para o final do primeiro segmento
  rotate(elbowAngle);
  fill(180);
  rect(armLength2 / 2, 0, armLength2, 20); // Segundo segmento do braço

  // Mão/Pulso
  translate(armLength2, 0); // Move para o final do segundo segmento
  rotate(wristAngle);
  fill(200);
  rect(handLength / 2, 0, handLength, 30); // Mão
  pop();
}