package com.dp;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;

@Entity
public class pen {
    @Id
    private int pid;
    private String pname;

    @ManyToOne
    private student student;

    public int getPid() {
        return this.pid;
    }

    public void setPid(int pid) {
        this.pid = pid;
    }

    public String getPname() {
        return this.pname;
    }

    public void setPname(String pname) {
        this.pname = pname;
    }

    public student getStudent() {
        return this.student;
    }

    public void setStudent(student student) {
        this.student = student;
    }

    public String toString() {
        return "Pen ID: " + pid + ", Pen Name: " + pname;
    }
}