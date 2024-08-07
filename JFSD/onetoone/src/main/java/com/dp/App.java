package com.dp;

import java.util.Scanner;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class App 
{
    public static void main( String[] args ){
        Scanner sc=new Scanner(System.in);

        Dept d = new Dept();
        System.out.println("Enter the Department ID:");
        d.setDid(sc.nextInt());
        System.out.println("Enter the Department Name:");
        d.setDname(sc.next());

        emp e = new emp();
        System.out.println("Enter the Employee ID:");
        e.setEid(sc.nextInt());
        System.out.println("Enter the Employee Name:");
        e.setEname(sc.next());
        e.setD(d);

        Configuration con = new Configuration().configure().addAnnotatedClass(emp.class);
        SessionFactory sf = con.buildSessionFactory();
        Session s = sf.openSession();
        Transaction t = s.beginTransaction();
        s.persist(d);
        s.persist(e);
        t.commit();
    }
}
