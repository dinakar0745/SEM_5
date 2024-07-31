package com.dp.servlet.servlet;

import com.dp.servlet.model.*;

import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;

@WebServlet("/employee")
public class EmployeeServlet extends HttpServlet {
    private List<Employee> employees = new ArrayList<>();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        out.println("<html><body>");
        out.println("<h2>Employee List</h2>");
        out.println("<ul>");
        for (Employee emp : employees) {
            out.println("<li>" + emp + "</li>");
        }
        out.println("</ul>");
        out.println("<h3>Add New Employee</h3>");
        out.println("<form method='post'>");
        out.println("ID: <input type='number' name='id' required><br>");
        out.println("Name: <input type='text' name='name' required><br>");
        out.println("Position: <input type='text' name='position' required><br>");
        out.println("<input type='submit' value='Add Employee'>");
        out.println("</form>");
        out.println("</body></html>");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        int id = Integer.parseInt(request.getParameter("id"));
        String name = request.getParameter("name");
        String position = request.getParameter("position");

        employees.add(new Employee(id, name, position));

        response.sendRedirect(request.getContextPath() + "/employee");
    }
}