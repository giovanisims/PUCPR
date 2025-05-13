function desenharTanque(x, y, rotacao, rotacaoTorre) {
    push();
    translate(x, y);
    rotate(rotacao);
  
    rectMode(CENTER); // Definir rectMode uma vez no início

    // Corpo do tanque
    fill(50, 80, 50); // Verde escuro
    rect(0, 0, 60, 40); // Retângulo principal do corpo
  
    // Esteiras
    fill(40); // Cinza escuro para esteiras
    rect(0, 25, 70, 10); // Esteira esquerda
    rect(0, -25, 70, 10); // Esteira esquerda
  
    // Torre
    push();
    rotate(rotacaoTorre);
    fill(80, 120, 80); // Verde um pouco mais claro para a torre
    rect(0, 0, 40, 30); // Base da torre
  
    // Canhão
    fill(60); // Cinza para o canhão
    rect(20, 0, 40, 8); // Canhão (ajustei a posição x para sair da torre)
    pop();
  
    pop();
  }
  
   let tanqueX, tanqueY, tanqueRotacao, torreRotacao;
   const VELOCIDADE_TANQUE = 2;
   const VELOCIDADE_ROTACAO = 3;
   const VELOCIDADE_ROTACAO_TORRE = 3;
 
   function setup() {
     createCanvas(400, 400);
     angleMode(DEGREES); // Usar graus para rotação
     tanqueX = width / 2;
     tanqueY = height / 2;
     tanqueRotacao = 0;
     torreRotacao = 0;
   }
   
   function draw() {
     background(220);
   
     // Controle do Tanque
     if (keyIsDown(UP_ARROW)) {
       tanqueX += VELOCIDADE_TANQUE * cos(tanqueRotacao);
       tanqueY += VELOCIDADE_TANQUE * sin(tanqueRotacao);
     }
     if (keyIsDown(DOWN_ARROW)) {
       tanqueX -= VELOCIDADE_TANQUE * cos(tanqueRotacao);
       tanqueY -= VELOCIDADE_TANQUE * sin(tanqueRotacao);
     }
     if (keyIsDown(LEFT_ARROW)) {
       tanqueRotacao -= VELOCIDADE_ROTACAO;
     }
     if (keyIsDown(RIGHT_ARROW)) {
       tanqueRotacao += VELOCIDADE_ROTACAO;
     }
   
     // Controle da Torre
     if (keyIsDown(65)) { // Tecla A
       torreRotacao -= VELOCIDADE_ROTACAO_TORRE;
     }
     if (keyIsDown(68)) { // Tecla D
       torreRotacao += VELOCIDADE_ROTACAO_TORRE;
     }
   
     desenharTanque(tanqueX, tanqueY, tanqueRotacao, torreRotacao);
   }