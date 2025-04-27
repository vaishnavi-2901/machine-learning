package com.example.demo.models.expense;

import java.util.List;

import com.example.demo.models.Split;
import com.example.demo.models.split.ExpenseMetaData;

public class EqualExpense extends Expense{

    public EqualExpense(String id, double amount, String paidByUserId, List<Split> splits,
            ExpenseMetaData expenseMetaData) {
        super(id, amount, paidByUserId, splits, expenseMetaData);
        //TODO Auto-generated constructor stub
    }

}
