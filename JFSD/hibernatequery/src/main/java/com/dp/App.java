package com.dp;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        student s = new student();
        System.out.println("Enter Student ID: ");
        s.setSid(sc.nextInt());
        System.out.println("Enter Student Name: ");
        s.setSname(sc.next());

        List<pen> pens = new ArrayList<>();
        for (int i = 0; i < 3; i++) { // Example: adding 3 pens
            pen p = new pen();
            System.out.println("Enter Pen ID: ");
            p.setPid(sc.nextInt());
            System.out.println("Enter Pen Name: ");
            p.setPname(sc.next());
            p.setStudent(s); // Set the student for each pen
            pens.add(p);
        }
        s.setPens(pens); // Set the list of pens in the student

        Configuration con = new Configuration().configure().addAnnotatedClass(student.class).addAnnotatedClass(pen.class);
        try (SessionFactory sf = con.buildSessionFactory();
             Session sx = sf.openSession()) {

            Transaction tx = sx.beginTransaction();
            sx.save(s); // Save the student object
            for (pen p : pens) {
                sx.save(p); // Save each pen object
            }
            tx.commit();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
