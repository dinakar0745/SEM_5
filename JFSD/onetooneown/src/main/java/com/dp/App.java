package com.dp;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import java.util.Scanner;

public class App 
{
    public static void main( String[] args )
    {
        Scanner sc = new Scanner(System.in);
        
        book b = new book();
        System.out.println("Enter Book ID: ");
        b.setBid(sc.nextInt());
        System.out.println("Enter Book Name: ");
        b.setBname(sc.next());
        System.out.println("Enter Author: ");
        b.setAuthor(sc.next());

        student s = new student();
        System.out.println("Enter Student ID: ");
        s.setSid(sc.nextInt());
        System.out.println("Enter Student Name: ");
        s.setSname(sc.next());
        s.setB(b);

        Configuration con = new Configuration().configure().addAnnotatedClass(student.class);
        SessionFactory sf = con.buildSessionFactory();
        Session sx = sf.openSession();
        Transaction tx = sx.beginTransaction();
        sx.save(b);
        sx.save(s);
        tx.commit();
        
    }
}
