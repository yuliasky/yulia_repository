Attribute VB_Name = "Module1"
Sub StockData()
    
    Dim ticker_array() As String
    Dim count_ticker As Integer
    Dim tmp_ticker As String
    Dim init As Double
    Dim vol As Double
    Dim open_val As Double
    Dim close_val As Double
    Dim prev_neg_val As Double
    Dim prev_pos_val As Double
    Dim prev_vol As Double
    Dim prev_neg_ticker As String
    Dim prev_pos_ticker As String
    Dim prev_vol_ticker As String
    
    count_ticker = 0
    tmp_ticker = ""
    lastrow = Cells(Rows.Count, "A").End(xlUp).Row
    
    For i = 2 To lastrow
        If Cells(i, 1).Value <> tmp_ticker Then
            tmp_ticker = Cells(i, 1)
            count_ticker = count_ticker + 1
        End If
    Next i
    
    MsgBox ("Number of tickers: " + Str(count_ticker))
    ReDim ticker_array(count_ticker)
    
    tmp_ticker = ""
    count_ticker = 0
    For i = 2 To lastrow
        If Cells(i, 1).Value <> tmp_ticker Then
            tmp_ticker = Cells(i, 1).Value
            ticker_array(count_ticker) = tmp_ticker
            count_ticker = count_ticker + 1
        End If
    Next i
    
    MsgBox ("Last ticker is: " + ticker_array(count_ticker - 1))
    
    lastcol = Cells(1, Columns.Count).End(xlToLeft).Column
    
    'Define Header
    Cells(1, lastcol + 2).Value = "Ticker"
    Cells(1, lastcol + 3).Value = "Yearly Change"
    Columns(lastcol + 3).AutoFit
    Cells(1, lastcol + 4).Value = "Percent Change"
    Columns(lastcol + 4).AutoFit
    Cells(1, lastcol + 5).Value = "Total Stock Volume"
    Columns(lastcol + 5).AutoFit
    
    'Insert table ticker array
    prev_neg_val = 0
    prev_pos_val = 0
    prev_vol = 0
    
    'Define init to not loop through the whole columns over and over again. Since tickers and dates are already in ascendent
    'order then that is not necessary, otherwise it will take lot of time to complete the execution
    init = 2
    For i = 0 To (count_ticker - 1)
        vol = 0
        open_val = 0
        For j = init To lastrow
            If Cells(j, 1).Value = ticker_array(i) Then
                vol = vol + Cells(j, lastcol)
                If open_val = 0 Then
                    open_val = Cells(j, 3).Value
                End If
                close_val = Cells(j, 6).Value
            Else
                init = j
                Exit For
            End If
        Next j
        Cells(i + 2, lastcol + 2).Value = ticker_array(i)
        Cells(i + 2, lastcol + 3).Value = close_val - open_val
        Cells(i + 2, lastcol + 3).NumberFormat = "0.###############"
        If open_val <> 0 Then
            Cells(i + 2, lastcol + 4).Value = FormatPercent((Cells(i + 2, lastcol + 3).Value / open_val), 2)
        Else
            Cells(i + 2, lastcol + 4).Value = FormatPercent((Cells(i + 2, lastcol + 3).Value), 2)
        End If
        If Cells(i + 2, lastcol + 3).Value < 0 Then
            Cells(i + 2, lastcol + 3).Interior.Color = vbRed
            If Cells(i + 2, lastcol + 4) < prev_neg_val Then
                prev_neg_val = Cells(i + 2, lastcol + 4)
                prev_neg_ticker = ticker_array(i)
            End If
        Else
            Cells(i + 2, lastcol + 3).Interior.Color = vbGreen
            If Cells(i + 2, lastcol + 4) > prev_pos_val Then
                prev_pos_val = Cells(i + 2, lastcol + 4)
                prev_pos_ticker = ticker_array(i)
            End If
        End If
        Cells(i + 2, lastcol + 5).Value = vol
        If vol > prev_vol Then
            prev_vol = vol
            prev_vol_ticker = ticker_array(i)
        End If
    Next i
    'To view the complete decimals and not #'s
    Columns(lastcol + 3).AutoFit
    
    'Insert table Greatest values
    lastcol = Cells(1, Columns.Count).End(xlToLeft).Column
    
    Cells(1, lastcol + 4).Value = "Ticker"
    Cells(1, lastcol + 5).Value = "Value"
    
    Cells(2, lastcol + 3).Value = "Greatest % Increase"
    Cells(3, lastcol + 3).Value = "Greatest % Decrease"
    Cells(4, lastcol + 3).Value = "Greatest Total Volume"
    Columns(lastcol + 3).AutoFit
    
    Cells(2, lastcol + 4).Value = prev_pos_ticker
    Cells(2, lastcol + 5).Value = FormatPercent(prev_pos_val, 2)
    Cells(3, lastcol + 4).Value = prev_neg_ticker
    Cells(3, lastcol + 5).Value = FormatPercent(prev_neg_val, 2)
    Cells(4, lastcol + 4).Value = prev_vol_ticker
    Cells(4, lastcol + 5).Value = prev_vol
    Columns(lastcol + 5).AutoFit




End Sub



