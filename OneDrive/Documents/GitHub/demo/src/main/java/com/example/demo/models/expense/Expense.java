package com.example.demo.models;

import java.util.List;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public abstract class Expense {
    String expenseId;
    double amount;
    ExpenseMetaData expenseMetaData;
    String paidByUserId;
    List<Split> splits;
    
    public Expense(String id,double amount, String paidByUserId, List<Split> splits, ExpenseMetaData expenseMetaData){
        this.expenseId = id;
        this.amount = amount;
        this.paidByUserId = paidByUserId;
        this.splits = splits;
        this.expenseMetaData = expenseMetaData;
    }
}