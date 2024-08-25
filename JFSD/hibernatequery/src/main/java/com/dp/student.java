package com.dp;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.JoinColumn;
import java.util.List;

@Entity
public class student {
    @Id
    private int sid;
    private String sname;

    @OneToMany
    @JoinColumn(name = "sid")
    private List<pen> pens;

    public List<pen> getPens() {
        return this.pens;
    }

    public void setPens(List<pen> pens) {
        this.pens = pens;
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