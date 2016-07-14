#include <stdio.h>
#include <string.h>
#include <math.h>

lawOfSines(side, angleA, angleC) {
	int newSide;
	newSide = side*(sin((angleA*3.14)/180))/sin((angleC*3.14)/180);

    return abs(newSide);
}

ThirdAngleCalc(angleA, angleB){
	int angleC;

    angleC = (180-(angleA+angleB));
    return angleC;
}

AAS() {
	int angleA;
	int angleB;
	int angleC;
	int sidea;
	int sideb;
	int sidec;

	puts("Enter your first angle:");
	scanf(" %d",&angleA);
	puts("Enter your second angle:");
	scanf(" %d",&angleC);
	puts("Enter your side:");
	scanf(" %d",&sidec);

	angleB = (180-(angleA+angleC));

	sidea = lawOfSines(sidec, angleA, angleC);
    sideb = lawOfSines(sidec, angleB, angleC);

    drawing(sidea, sideb, sidec, angleA, angleB, angleC);
}

ASA() {
	int angleA;
	int angleB;
	int angleC;
	int sidea;
	int sideb;
	int sidec;

	puts("Enter your first angle:");
	scanf(" %d",&angleA);
	puts("Enter your second angle:");
	scanf(" %d",&angleB);
	puts("Enter your side:");
	scanf(" %d",&sidec);

    angleC = (180-(angleA+angleB));
    
    sidea = lawOfSines(sidec, angleA, angleC);
    sideb = lawOfSines(sidec, angleB, angleC);

    drawing(sidea, sideb, sidec, angleA, angleB, angleC);
}

SAS(){
	int angleA;
	int angleB;
	int angleC;
	int sidea;
	int sideb;
	int sidec;
	int hold;

	puts("Enter your first angle:");
	scanf(" %d",&angleA);
	puts("Enter your first side:");
	scanf(" %d",&sideb);
	puts("Enter your second side:");
	scanf(" %d",&sidec);

    if(sideb>sidec){
        hold = sidec;
        sidec = sideb;
        sideb = hold;
    }

    sidea = sqrt((sideb*sideb)+(sidec*sidec)-((2*sideb*sidec)*(cos((3.14/180)*(angleA)))));

    angleB = (180/3.14)*(asin(((sin((3.14/180)*(angleA))*sideb)/sidea)));

    angleC = 180-(angleA+angleB);

    drawing(sidea, sideb, sidec, angleA, angleB, angleC);
}

SSS(){
	float angleA;
	float angleB;
	float angleC;
	float sidea;
	float sideb;
	float sidec;

	puts("Enter your first side:");
	scanf(" %f",&sidea);
	puts("Enter your second side:");
	scanf(" %f",&sideb);
	puts("Enter your third side:");
	scanf(" %f",&sidec);

    angleA = (180/3.14)*acos((((sideb*sideb)+(sidec*sidec))-(sidea*sidea))/(2*sideb*sidec));

    angleB = (180/3.14)*acos((((sidec*sidec)+(sidea*sidea))-(sideb*sideb))/(2*sidec*sidea));

    angleC = ThirdAngleCalc((int)angleA,(int)angleB);
    
    drawing((int)sidea, (int)sideb, (int)sidec, (int)angleA, (int)angleB, (int)angleC);
}

drawing(sidea, sideb, sidec, angleA, angleB, angleC) {

    printf("Your sides are:\t %d \t %d \t %d \n", sidea, sideb, sidec);
    printf("And your angles are:\t %d \t %d \t %d \n", angleA, angleB, angleC);

    if(sidea==sideb && sideb==sidec){
        puts("You made an equillateral triangle!");
    }
    else if(angleA==90 || angleB==90 || angleC==90){
        puts("You made a right triangle!");
    }
    else if(angleA==angleB || angleB==angleC || angleC==angleA){
        puts("You made an isoceles triangle!");
    }
    else if(sidea!=sideb && sideb!=sidec && sidec!=sidea){
        puts("You made a scalene triangle!");
    }

}

main() {
	char query;
	int response;
	do {
		puts("Would you like to draw a triangle? (Y/N)");
		scanf(" %c",&query); query = toupper(query);
		if(query == 'Y'){
			do {
				puts("Select how you would like to define your triangle:");
				puts("1 - AAS");
				puts("2 - ASA");
				puts("3 - SAS");
				puts("4 - SSS");
				puts("5 - HL");
				scanf(" %d",&response);

				if(response == 1){
					AAS();
					break;
				}
				else if(response == 2){
					ASA();
					break;
				}
				else if(response == 3){
					SAS();
					break;
				}
				else if(response == 4){
					SSS();
					break;
				}
				else if(response == 5){
					puts("HL");
					break;
				}

			} while(response != 1 || response != 2 || response != 3 || response != 4 || response != 5);
		}
	} while(query == 'Y');
}