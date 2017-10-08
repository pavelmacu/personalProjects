unsigned int dato;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
      while(Serial.available()>0){  //Comprobamos que la comunicacion serial este disponible.
        dato=Serial.read(); //Leemos
        if(dato=='Y')digitalWrite(13,HIGH);
        else if(dato=='N')digitalWrite(13,LOW);
        else if (dato=='H'){
          Serial.println("espponse");
        }
        else{}
      }
}
