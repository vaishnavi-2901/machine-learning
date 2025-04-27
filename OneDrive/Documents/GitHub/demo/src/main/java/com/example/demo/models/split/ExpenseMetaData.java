package com.example.demo.models;

public class ExpenseMetaData {
    String name;
    byte imageUrl;
    String description;

    public ExpenseMetaData(String name, String imageUrl, String description){
        this.name = name;
        this.imageUrl = imageUrl;
        this.description = description;
    }
}
