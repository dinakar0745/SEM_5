package com.dp;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import java.util.Scanner;

public class App {
  public static void main(String[] args) {
    Configuration con = new Configuration().configure().addAnnotatedClass(student.class);
    SessionFactory sf = con.buildSessionFactory();

    Scanner sc = new Scanner(System.in);
    int choice = 0;

    while (choice != 5) {
      System.out.println("1. Create Student");
      System.out.println("2. Read Student");
      System.out.println("3. Update Student");
      System.out.println("4. Delete Student");
      System.out.println("5. Exit");
      System.out.print("Enter your choice: ");
      choice = sc.nextInt();

      switch (choice) {
        case 1:
          createStudent(sf, sc);
          break;
        case 2:
          readStudent(sf, sc);
          break;
        case 3:
          updateStudent(sf, sc);
          break;
        case 4:
          deleteStudent(sf, sc);
          break;
        case 5:
          System.out.println("Exiting...");
          break;
        default:
          System.out.println("Invalid choice. Please try again.");
          break;
      }
    }
    sf.close();
  }

  public static void createStudent(SessionFactory sf, Scanner scanner) {
    System.out.print("Enter student ID: ");
    int id = scanner.nextInt();
    scanner.nextLine(); // Consume the newline character

    System.out.print("Enter student name: ");
    String name = scanner.nextLine();

    System.out.print("Enter student marks: ");
    int marks = scanner.nextInt();

    Session s = sf.openSession();
    Transaction t = s.beginTransaction();

    student st = new student();
    st.setSid(id);
    st.setSname(name);
    st.setMarks(marks);

    s.persist(st);
    t.commit();
    s.close();

    System.out.println("Student created successfully.");
  }

  public static void readStudent(SessionFactory sf, Scanner scanner) {
    System.out.print("Enter student ID: ");
    int id = scanner.nextInt();

    Session s = sf.openSession();
    student st = s.get(student.class, id);
    s.close();

    if (st != null) {
      System.out.println("Student: " + st.getSname() + ", Marks: " + st.getMarks());
    } else {
      System.out.println("Student not found.");
    }
  }

  public static void updateStudent(SessionFactory sf, Scanner scanner) {
    System.out.print("Enter student ID: ");
    int id = scanner.nextInt();
    scanner.nextLine(); // Consume the newline character

    Session s = sf.openSession();
    Transaction t = s.beginTransaction();

    student st = s.get(student.class, id);
    if (st != null) {
      System.out.print("Enter new student name: ");
      String name = scanner.nextLine();

      System.out.print("Enter new student marks: ");
      int marks = scanner.nextInt();

      st.setSname(name);
      st.setMarks(marks);
      s.merge(st);

      t.commit();
      System.out.println("Student updated successfully.");
    } else {
      System.out.println("Student not found.");
    }

    s.close();
  }

  public static void deleteStudent(SessionFactory sf, Scanner scanner) {
    System.out.print("Enter student ID: ");
    int id = scanner.nextInt();

    Session s = sf.openSession();
    Transaction t = s.beginTransaction();

    student st = s.get(student.class, id);
    if (st != null) {
      s.remove(st);
      t.commit();
      System.out.println("Student deleted successfully.");
    } else {
      System.out.println("Student not found.");
    }

    s.close();
  }
}