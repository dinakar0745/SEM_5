package com.dp;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToOne;

@Entity
public class student {
    @Id
    private int sid;
    private String sname;

    @OneToOne
    @JoinColumn(name = "bid")

    private book b;

    public book getB() {
        return this.b;
    }

    public void setB(book b) {
        this.b = b;
    }

    public int getSid() {
        return this.sid;
    }

    public void setSid(int sid) {
        this.sid = sid;
    }

    public String getSname() {
        return this.sname;
    }

    public void setSname(String sname) {
        this.sname = sname;
    }

    public String toString() {
        return "Student ID: " + sid + ", Student Name: " + sname;
    }
}
