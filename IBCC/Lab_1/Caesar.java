package Lab_1;

import java.util.Scanner;

public class Caesar {
    // x=c-a
    // x+shift mod 26
    public static String encrypt(String text, int shift) {
        String result = "";
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (Character.isUpperCase(c)) {
                result += (char)((c - 'A' + shift) % 26 + 'A');
            } else if (Character.isLowerCase(c)) {
                result += (char)((c - 'a' + shift) % 26 + 'a');
            } else {
                result += c;
            }
        }
        return result;
    }

    // x=c+a
    public static String decrypt(String text, int shift) {
        return encrypt(text, 26 - shift);
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Text: ");
        String t=sc.nextLine();
        System.out.println("Enter the Shift Value: ");
        int shift=sc.nextInt();
        String enc=encrypt(t,shift);
        System.out.println("Encrypted Text:" + enc);
        System.out.println("Decrypted Text:" + decrypt(enc,shift));
    }
}
