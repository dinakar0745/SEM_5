package com.dp;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToOne;

@Entity
public class emp {
    @Id
    private int eid;
    private String ename;

    @OneToOne
    @JoinColumn(name = "did")
    private Dept d;

    public Dept getD() {
        return this.d;
    }

    public void setD(Dept d) {
        this.d = d;
    }

    public int getEid() {
        return this.eid;
    }

    public void setEid(int eid) {
        this.eid = eid;
    }

    public String getEname() {
        return this.ename;
    }

    public void setEname(String ename) {
        this.ename = ename;
    }

    @Override
    public String toString() {
        return "Employee [eid=" + eid + ", ename=" + ename + ", d=" + d + "]";
    }
}
