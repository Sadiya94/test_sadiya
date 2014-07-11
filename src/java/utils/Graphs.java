import java.util.Scanner;
public class Graphs{
    public static void main(String[] args){
        Scanner k = new Scanner(System.in);
        int[] a = new int[5];
        System.out.println("Enter 5 numbers");
        for(int i=0;i<a.length;i++){
            a[i]=k.nextInt();
        }
        for(int i=0;i<a.length;i++){
            for(int j=0;j<a[i];j++)
               System.out.print(a[i]);
            System.out.println();
        }
    }
}