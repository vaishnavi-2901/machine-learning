package com.example.demo.models;

import com.example.demo.models.split.User;


public abstract class Split {
    double amount;
    String userId;
    protected User user;


    public Split(double amount, String userId){
        this.amount = amount;
        this.userId = userId;
    }

    public User getUser(){
        return user;
    }
    public double getAmount(){
        return amount;
    }
}
