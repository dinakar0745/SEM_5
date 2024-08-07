package com.dp;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class book {
    @Id
    private int bid;
    private String bname;
    private String author;

    public int getBid() {
        return this.bid;
    }

    public void setBid(int bid) {
        this.bid = bid;
    }

    public String getBname() {
        return this.bname;
    }

    public void setBname(String bname) {
        this.bname = bname;
    }

    public String getAuthor() {
        return this.author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String toString() {
        return "Book ID: " + bid + ", Book Name: " + bname + ", Author: " + author;
    }
    
}
