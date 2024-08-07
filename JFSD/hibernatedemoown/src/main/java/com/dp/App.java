package com.dp;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import java.util.Scanner;


public class App{
    public static void main( String[] args )
    {
        Configuration con = new Configuration().configure().addAnnotatedClass(name.class);
        SessionFactory sf = con.buildSessionFactory();
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the first name: ");
        String fname = sc.nextLine();
        System.out.println("Enter the middle name: ");
        String mname = sc.nextLine();
        System.out.println("Enter the last name: ");
        String lname = sc.nextLine();

        Session s = sf.openSession();
        Transaction t = s.beginTransaction();
        name n = new name();

        n.setFirstName(fname);
        n.setMiddleName(mname);
        n.setLastName(lname);

        s.persist(n);
        t.commit();
        s.close();

        System.out.println("Name created successfully.");
    }
}
