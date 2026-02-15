// ===== Encoder Pins =====
#define encoderA 2   // MUST be interrupt pin
#define encoderB 4

volatile long pulse_count = 0;

// Interrupt function
void encoderISR()
{
  pulse_count++;
}

void setup()
{
  Serial.begin(115200);

  pinMode(encoderA, INPUT_PULLUP);
  pinMode(encoderB, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(encoderA), encoderISR, RISING);

  Serial.println("Rotate wheel exactly 1 full revolution.");
  Serial.println("Then type 'r' and press ENTER.");
}

void loop()
{
  if (Serial.available())
  {
    char cmd = Serial.read();

    if (cmd == 'r')
    {
      detachInterrupt(digitalPinToInterrupt(encoderA));

      Serial.print("Pulses counted: ");
      Serial.println(pulse_count);

      Serial.println("Resetting counter...");
      pulse_count = 0;

      attachInterrupt(digitalPinToInterrupt(encoderA), encoderISR, RISING);
    }
  }
}