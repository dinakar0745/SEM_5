package com.dp;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class Dept {
    @Id
    private int did;
    private String dname;

    public int getDid() {
        return this.did;
    }

    public void setDid(int did) {
        this.did = did;
    }

    public String getDname() {
        return this.dname;
    }

    public void setDname(String dname) {
        this.dname = dname;
    }
}
