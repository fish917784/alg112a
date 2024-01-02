#include <Arduino.h>
#include "PinDefinitionsAndMore.h"
#include <IRremote.hpp>

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
int answer[4], guess[4];
int length = 0;

void setup()
{
    Serial.begin(115200);
    Serial.println(F("START " __FILE__ " from " __DATE__ "\r\nUsing library version " VERSION_IRREMOTE));
    IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);
    Serial.print(F("Ready to receive IR signals of protocols: "));
    printActiveIRProtocols(&Serial);
    Serial.println(F("at pin " STR(IR_RECEIVE_PIN)));
    pinMode(4, OUTPUT);

    lcd.init();
    lcd.backlight();

    for (int i = 0; i < 4; i++)
    {
        answer[i] = random(10);

        for (int j = 0; j < i; j++)
        {
            if (answer[i] == answer[j])
            {
                i--;
                break;
            }
        }
    }
}

void loop()
{
    if (length < 4)
    {
        lcd.setCursor(0, 0);
        lcd.print("ENTER NUMBER:");

        if (length == 0)
        {
            lcd.setCursor(0, 1);
            lcd.print("----");
        }

        if (IrReceiver.decode())
        {
            IrReceiver.printIRResultShort(&Serial);
            IrReceiver.printIRSendUsage(&Serial);

            if (IrReceiver.decodedIRData.protocol == UNKNOWN)
            {
                Serial.println(F("Received noise or an unknown (or not yet enabled) protocol"));
                IrReceiver.printIRResultRawFormatted(&Serial, true);
            }

            Serial.println();
            IrReceiver.resume();

            int number = 0;

            if (IrReceiver.decodedIRData.command == 0x0) // 0
            {
                number = 0;
            }
            else if (IrReceiver.decodedIRData.command == 0x0) // 1
            {
                number = 1;
            }
            else if (IrReceiver.decodedIRData.command == 0x0) // 2
            {
                number = 2;
            }
            else if (IrReceiver.decodedIRData.command == 0x0) // 3
            {
                number = 3;
            }
            else if (IrReceiver.decodedIRData.command == 0x0) // 4
            {
                number = 4;
            }
            else if (IrReceiver.decodedIRData.command == 0x0) // 5
            {
                number = 5;
            }
            else if (IrReceiver.decodedIRData.command == 0x0) // 6
            {
                number = 6;
            }
            else if (IrReceiver.decodedIRData.command == 0x0) // 7
            {
                number = 7;
            }
            else if (IrReceiver.decodedIRData.command == 0x0) // 8
            {
                number = 8;
            }
            else if (IrReceiver.decodedIRData.command == 0x0) // 9
            {
                number = 9;
            }

            for (int i = 0; i < length; i++)
            {
                if (guess[i] == number)
                {
                    return;
                }
            }

            lcd.setCursor(length, 1);
            lcd.print(number + '0');
            guess[length] = number;
            length++;
        }
    }
    else
    {
        int a = 0, b = 0;

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (i == j && answer[i] == guess[j])
                {
                    a++;
                }

                if (i != j && answer[i] == guess[j])
                {
                    b++;
                }
            }
        }

        if (a == 4)
        {
            lcd.setCursor(0, 0);
            lcd.print("YOU WIN");
        }
        else
        {
            lcd.setCursor(0, 0);
            lcd.print(a + '0');
            lcd.setCursor(1, 0);
            lcd.print("A");
            lcd.setCursor(2, 0);
            lcd.print(b + '0');
            lcd.setCursor(3, 0);
            lcd.print("B");
            delay(1000);
            length = 0;
        }
    }
}
