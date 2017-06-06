/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaalpha;
import java.sql.*;
/**
 *
 * @author avos
 */
public class kunci {
    public static Connection key(){
        Connection jacon = null;
        try {
            String url = "jdbc:sqlite:D://AvosLab/JavaAlpha/alpha.db";
            jacon = DriverManager.getConnection(url);
            System.out.println("Connection Granted");
        } catch (Exception e) {
            System.out.println("Connection Error");
        }
        return jacon;
    }
}
