/* 
let c1Pos, c2Pos;
let c1Vel,c2Vel;

function setup() {
    createCanvas(600,500);
    c1Pos = createVector(100,50);
    c2Pos = createVector(400,300);

    c1Vel = createVector(2,2);
    c2Vel = p5.Vector.fromAngle(radians(240),2);
}

function draw() {
    background(0);

    c1Pos.add(c1Vel);
    fill("red");
    circle(c1Pos.x,c1Pos.y,25);

    c2Pos.add(c2Vel);
    fill("blue");
    circle(c2Pos.x,c2Pos.y,25);
}
 */

/* 
// Atividade 1

let c1pos, c2Pos;
let c2Vel;
let angle = 0;
let OFFSET = 30;

function setup() {
    createCanvas(500,500);
    c1pos = createVector(mouseX, mouseY);
    c2Pos = createVector(c1pos.x, c1pos.y);
}


function draw() {
    background(0)

    fill("yellow");
    circle(c1pos.x = mouseX, c1pos.y = mouseY, 40);


    translate(c1pos.x, c1pos.y);

    rotate(angle);

    fill("blue");
    circle(OFFSET, OFFSET, 20);


    angle += 0.02;
}

 */

let c1pos;
let clickpos;
let distance;
let SPEED = 5;
let isMouseClicked = false;
let tolerance = 5; // Adjust this value to control how close the circle needs to be to the click position

function setup() {
    createCanvas(500, 500);
    c1pos = createVector(250, 250);
    clickpos = createVector(c1pos.x, c1pos.y);
}

function draw() {
    background(0);

    fill("red");
    circle(c1pos.x, c1pos.y, 50);

    if (mouseIsPressed && !isMouseClicked) {
        isMouseClicked = true;

        clickpos.x = mouseX;
        clickpos.y = mouseY;
        console.log(`mouse was pressed x: ${mouseX} y: ${mouseY}`)
    }

    if (isMouseClicked) {
        distance = p5.Vector.sub(clickpos, c1pos);
        if (distance.mag() > tolerance) { 
            distance.setMag(SPEED);
            c1pos.add(distance);
        } else {
            isMouseClicked = false;
        }
    }
}