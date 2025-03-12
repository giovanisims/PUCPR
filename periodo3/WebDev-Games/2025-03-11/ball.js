function setup() {
    createCanvas(600, 500);
}
/* 
let x1 = 100;
let y1 = 100;
const SPEED = 5;
const BALL_RADIUS = 50; // Half of the circle's diameter

function draw() {
    background(0);
    stroke(255);

    fill(mouseIsPressed ? "red" : "green");
    circle(mouseX, mouseY, 100, 100);

    fill("red");
    circle(x1, y1, 100, 100);

    // Movement controls without the restrictive condition
    if (keyIsDown(UP_ARROW)) {
        y1 -= SPEED;
    }
    if (keyIsDown(DOWN_ARROW)) {
        y1 += SPEED;
    }
    if (keyIsDown(LEFT_ARROW)) {
        x1 -= SPEED;
    }
    if (keyIsDown(RIGHT_ARROW)) {
        x1 += SPEED;
    }
    
    x1 = constrain(x1, BALL_RADIUS, width - BALL_RADIUS);
    y1 = constrain(y1, BALL_RADIUS, height - BALL_RADIUS);
} */

    
    let x1 = 100;
    let y1 = 100;
    let targetX = x1;
    let targetY = y1;
    const SPEED = 5;
    const BALL_RADIUS = 50;
    let isMoving = false;
    
    function draw() {
        background(0);
        stroke(255);
    
        fill("green");
        circle(x1, y1, 100);
        
        // Move ball toward target if we have a target
        if (isMoving) {
            // Calculate direction vector
            let dx = targetX - x1;
            let dy = targetY - y1;
            
            // Calculate distance to target
            let distance = sqrt(dx*dx + dy*dy);
            
            // If we're very close to the target, stop moving
            if (distance < SPEED) {
                x1 = targetX;
                y1 = targetY;
                isMoving = false;
            } else {
                // Normalize the direction vector and multiply by speed
                dx = (dx / distance) * SPEED;
                dy = (dy / distance) * SPEED;
                
                // Update position
                x1 += dx;
                y1 += dy;
            }
        }
        
        x1 = constrain(x1, BALL_RADIUS, width - BALL_RADIUS);
        y1 = constrain(y1, BALL_RADIUS, height - BALL_RADIUS);
    }
    
    function mousePressed() {
        targetX = mouseX;
        targetY = mouseY;
        isMoving = true;
        return false; 
    }