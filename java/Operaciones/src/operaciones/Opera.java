/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package operaciones;

/**
 *
 * @author luis
 */
public class Opera {
    //Declaramos atributos
    int a, b;
    
    //Metodos declarados
    
    int suma(int a, int b){
    return (a+b);
    }
    
    int resta(int x,int y){
        return(x-y);
    }
    
    int multiplicar(int x,int y){
        return(x*y);
    }
    double dividir(double x,double y){
        return(x/y);
    }
    double AreaCirculo(int radio){
        return(3.1416*(radio*radio));
    }    
    boolean estado(int cervezas){
        boolean e=false;
        if(cervezas>=5){
            e=true;
        }else
        {
            e=false;
        }
        return e;
    }
}
