package Lab_1;

import java.util.Scanner;

public class Affine {
    // ax+b mod 26
    public static String encrypt(String text, int a, int b) {
        String result = "";
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (Character.isUpperCase(c)) {
                result += (char)((a * (c - 'A') + b) % 26 + 'A');
            } else if (Character.isLowerCase(c)) {
                result += (char)((a * (c - 'a') + b) % 26 + 'a');
            } else {
                result += c;
            }
        }
        return result;
    }

    // a_inv(x-b) mod 26
    public static String decrypt(String text, int a, int b) {
        String result = "";
        int a_inv = 0;
        for (int i = 0; i < 26; i++) {
            if ((a * i) % 26 == 1) {
                a_inv = i;
                break;
            }
        }
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (Character.isUpperCase(c)) {
                result += (char)((a_inv * (c - 'A' - b + 26) % 26) + 'A');
            } else if (Character.isLowerCase(c)) {
                result += (char)((a_inv * (c - 'a' - b + 26) % 26) + 'a');
            } else {
                result += c;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Text: ");
        String t=sc.nextLine();
        System.out.println("Enter the Value of a: ");
        int a=sc.nextInt();
        System.out.println("Enter the Value of b: ");
        int b=sc.nextInt();
        String enc=encrypt(t,a,b);
        System.out.println("Encrypted Text:" + enc);
        System.out.println("Decrypted Text:" + decrypt(enc,a,b));
    }
}
