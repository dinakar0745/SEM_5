package Lab_1;

import java.math.BigInteger;
import java.util.Random;


public class MillerRabin {
    private static final int MAX_ITERATIONS = 5;

    public static boolean isPrime(BigInteger n) {
        if (n.compareTo(BigInteger.ONE) <= 0) {
            return false;
        }

        if (n.compareTo(BigInteger.valueOf(3)) <= 0) {
            return true;
        }

        int s = 0;
        BigInteger d = n.subtract(BigInteger.ONE);
        while (d.mod(BigInteger.TWO).equals(BigInteger.ZERO)) {
            s++;
            d = d.divide(BigInteger.TWO);
        }

        for (int i = 0; i < MAX_ITERATIONS; i++) {
            BigInteger a = getRandomBase(n);
            BigInteger x = a.modPow(d, n);

            if (x.equals(BigInteger.ONE) || x.equals(n.subtract(BigInteger.ONE))) {
                continue;
            }

            boolean isWitness = true;
            for (int r = 1; r < s; r++) {
                x = x.modPow(BigInteger.TWO, n);
                if (x.equals(BigInteger.ONE)) {
                    return false;
                }
                if (x.equals(n.subtract(BigInteger.ONE))) {
                    isWitness = false;
                    break;
                }
            }

            if (isWitness) {
                return false;
            }
        }

        return true;
    }

    private static BigInteger getRandomBase(BigInteger n) {
        Random rand = new Random();
        BigInteger result;
        do {
            result = new BigInteger(n.bitLength(), rand);
        } while (result.compareTo(n) >= 0 || result.compareTo(BigInteger.ONE) <= 0);
        return result;
    }
    
    //n > 1
    //n <= 3
    //d = n - 1
    //s = number of times d can be divided by 2
    //a = random base
    //x = a^d mod n
    //x = 1 or x = n - 1
    //x = x^2 mod n
    //x = 1
    //x = n - 1
    //n is prime
    //n is composite

    public static void main(String[] args) {
        BigInteger number = new BigInteger("123456789");
        boolean isPrime = isPrime(number);
        System.out.println(number + " is prime: " + isPrime);
    }
}
