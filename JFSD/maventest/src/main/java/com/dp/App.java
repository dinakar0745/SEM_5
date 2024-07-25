package com.dp;
import java.sql.PreparedStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class App 
{
    public static void main( String[] args ) throws SQLException
    {
        //1.load and register driver
        try {
            Class.forName("com.mysql.jdbc.Driver");
            //2.establish connection
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/cyber","root","");
            PreparedStatement st = con.prepareStatement("INSERT INTO cs values(1,'dp','hyd')");
            st.executeUpdate();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        
    }
}
