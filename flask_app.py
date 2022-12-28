from flask import Flask, request
from processing import calculate_real_gains, convert_raw_date, calculate_nominal_gains

app = Flask(__name__)

@app.route("/realgains", methods=["GET", "POST"])




def realgains():

#cheks if the input from the forms is appropriate

    errors = ""
    if request.method == "POST":
        past_unit_price_input = None
        raw_date = request.form["raw_date_form"]
        unit_price_input = None
        past_unit_price_input_date = None
        try:
            past_unit_price_input = float(request.form["past_price_per_unit_form"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["past_price_per_unit_form"])
        try:
            unit_price_input = float(request.form["current_price_per_unit_form"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["current_price_per_unit_form"])
        if past_unit_price_input is not None and unit_price_input is not None and raw_date is not None:




            #converts the YYYY-MM-DD date format to M/D/YYYY to be used in searching the Fred API database

            past_unit_price_input_date = convert_raw_date(raw_date)

            result = calculate_real_gains(past_unit_price_input, past_unit_price_input_date, unit_price_input)

            nominal_result = calculate_nominal_gains(past_unit_price_input, unit_price_input)

            return '''
                <html>
                <link rel="stylesheet" href='/staticFiles/main.css' />
                    <body>
                        <p>The nominal gains on this asset over the given time period are: {nominal_result}% </br>
                        the M2-adjusted real gains for this asset over the given time period are: {result}% </p>
                        <p><form action="/realgains">
                        <input type="submit" value="Return" />
                        </form></p>
                    </body>
                </html>
            '''.format(result=result, nominal_result=nominal_result)



    return '''
        <html lang="en">
        <link rel="stylesheet" href='/staticFiles/main.css' />
        <title>Real Gains</title>

            <body>

            <!-- explanation of the tool and it's purpose -->

            <h1 class = "realgains">    &nbsp;    Real Gains:</h1>
            <p><font size="+1">This is a simple calculator made to measure the value increase of an asset in relationship to the money supply.<br/>
            <br/>
            Inflation as measured through the CPI is a highly innacurate measurement of loss in total purchasing power,<br/>
            this is because it merely accounts for the nominal price changes in the final goods and services provided to the consumer.<br/>
            Such a measurement does not account for the loss in purchasing power for businesses in the form of materials, <br/>goods and services that precede the consumer market.<br/>
            Which in turn makes adjusting for inflation alone an inefficient way of judging the success of an investment. </br>
            <br/>

            Here, we are calculating the value of an asset as a ratio between it's nominal value in US dollars and the M2 money supply. <br/>
            This allows us to measure increases or decreases in its value as a share of the total purchasing power, rather than simply nominal changes.<br/>
            </br>
             Type the price of an asset in a given date in the past, select that date, and then type in the current price of said asset.

            </font></p>



                {errors}
                <form method="post" class = "calculator" action="http://caiomaltacoutinho.pythonanywhere.com/realgains">
                    <p> <h2 class="pppu"> Past unit price and date of measurement</h2></p>
                    <p><input type = "number" name="past_price_per_unit_form" /> <input type="date" name="raw_date_form" min='1980-11-03' max='2021-02-01'/> </p>
                    <p> <h2 class="ppu">Current unit price</h2></p>
                    <p><input type = "number" name="current_price_per_unit_form"</p>
                    <p><input type="submit" value="Calculate"/></p>
                </form>

           <!-- #explanation for possibly innacurate data and limited date range -->

            <p><font size="-1">
            *the past measurements of the M2 supply are limited to what is provided through the Federal Reserve Bank Of St. Louis's API, currently,</br>
            this means past prices can only be measured as recently as February 1st, 2021. </br>
            *the current M2 supply used in the calculation comes from the lastest update of the federalreserve.gov Money Stock Measures: </br>
            https://www.federalreserve.gov/releases/h6/current/default.htm
            </font></p>

            </body>
        </html>
    '''.format(errors=errors)
