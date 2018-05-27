/*
 * Compile: gcc -Wall -o rf rf.c -lwiringPi
 * Usage: sudo ./rf [binary] [delay in microseconds] [inverting bits]
 * Example.. turning on Silvercrest outlet A
 * sudo ./rf 11111111111111001001011001011011011011001011011011011011001001011001011011011011011011000000 500 1
 */ 

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <wiringPi.h>

#define PIN   0

void parse_bin(char *string, char *d, int invert, int repeat) {
   int len = strlen(string), delay = atoi(d);;
   int i; 
   while(repeat) {
            for(i=0; i < len; i ++) {
                digitalWrite( PIN, ((int)string[i] - 48) ^ invert );  
                delayMicroseconds(300);
                digitalWrite(PIN,0);
                delayMicroseconds(200);
            }
        repeat --;
        }
}

void reset_pin(void) {
   digitalWrite( PIN, LOW );
}

int main(int argc, char** argv) {
    int invert = 0;
                
    if(argc < 3) {
      printf("[bin] [delay] [invert]\n");
   return -1;      
   } 
    
    if(argv[3][0] == 49) 
      invert = 1;
       
    wiringPiSetup ();
    pinMode (PIN, OUTPUT);    
        
   reset_pin();
   parse_bin(argv[1], argv[2], invert, 4);
   reset_pin();
   
return 0;
}
