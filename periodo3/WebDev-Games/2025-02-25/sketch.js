function setup() {
    createCanvas(700, 700);
}
/* 
 function draw() {
 background("rebeccapurple");
 fill(255,0,0,100);
 circle(250,250,150);
 fill(0,255,0,100)
 circle(350,250,150)
 }
 */

/* 
 function draw() {
     background(255);
     for(var x = 0; x < 5; x++) {
         for(var y = 0; y < 5; y++) {
             circle( 60 + x * 120, 60 + y * 120 , 80)
             fill(50 + x * 40, 50 + y * 40, 127);
         }
     }
} */

 function draw() {
    background(0,127,255,10);
    noStroke()

    fill(252, 169, 39,255);
    circle(0,0,700);
    fill(251, 161, 41,255);
    circle(0,0,400);
    fill(250, 137, 35,255)
    circle(0,0,300);

    fill(107, 70, 20);
    arc(400, 500, 300, 200, 0, PI);

    stroke(107, 70, 20);
    strokeWeight(20);
    line(400,500,400,300);
    stroke(77, 50, 15);
    line(250,500,550,500);

    noStroke();
    fill(255, 255, 255);
    triangle(400, 300,    // Top point (where mast ends)
            400, 450,     // Bottom point (where mast starts)
            500, 450);
    
            noStroke();
            fill(0, 127, 255, 255);
            circle(250, 580, 60);
            circle(350, 590, 70);
            circle(450, 575, 65);
            circle(550, 585, 60);
            circle(300, 600, 55);
            circle(400, 595, 70);
            circle(500, 605, 65);

 }