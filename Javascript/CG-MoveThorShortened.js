//CodinGame. Same challenge as MoveThor.py
//Minified in JS. Each character counts. Not meant for readability.

var inputs=readline().split(' '),LX=parseInt(inputs[0]),LY=parseInt(inputs[1]),TX=parseInt(inputs[2]),TY=parseInt(inputs[3]),X=LX-TX,Y=LY-TY;
while(true){var e=parseInt(readline()),v='',h='';if(Y>0){v="S";Y-=1;}else if(Y<0){v="N";Y+=1;}if(X>0){h="E";X+=1;}else if(X<0){h="W";X-=1;}print(v+h);}
