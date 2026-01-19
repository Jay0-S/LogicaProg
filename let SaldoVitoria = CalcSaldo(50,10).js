let SaldoVitoria = CalcSaldo(50,10)

let Nivel

if (SaldoVitoria <= 10){
	Nivel=("Ferro")  
	}
else if(SaldoVitoria <=20){
	Nivel=("Bronze")
	}    
else if(SaldoVitoria <=50){
	Nivel=("Prata")	
    }
else if(SaldoVitoria <=80){
	Nivel=("Ouro")
    }
else if(SaldoVitoria <=90){
	Nivel=("Diamante")
	}
else if(SaldoVitoria <=100){
	Nivel=("Lendario")
    }
else {Nivel=("Imortal")	    
	}
function CalcSaldo(QuantV, QuantD){
	return QuantV-QuantD

}

console.log("O Herói tem de Saldo de vitórias ", SaldoVitoria , "e está no nível ", Nivel)