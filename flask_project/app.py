from flask import Flask, render_template, jsonify
import utils

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/time')
def get_time():
    return utils.get_time()


@app.route('/m1')
def get_m1_data():
    data = utils.get_new_store_num()
    data_order = utils.get_order_data()
    return jsonify(
        {"sum_total": data_order[0], "fre": data_order[1], "per_retailer": data_order[2], "new_store": data[0]})


@app.route('/m2')
def get_m2_data():
    res = []
    for tup in utils.get_map_data():
        # res.append({"name": tup[0], "value": int(tup[1])/100000})
        res.append({"name": tup[0], "value": int(tup[1])})
    min_num = utils.get_map_range_data()[0][1]
    # max_num = utils.get_map_range_data()[0][0]/100000
    max_num = utils.get_map_range_data()[0][0]
    return jsonify({"data": res, "max_num": max_num, "min_num": min_num})
    # return jsonify({"data": res})


@app.route('/l1')
def get_l1_data():
    sku = []
    num = []
    for s, n in utils.get_l1_data():
        sku.append(s)
        # num.append(int(n/100000))
        num.append(int(n))
    return jsonify({'sku': sku,
                    'num': num})


@app.route('/rl')
def get_rl_data():
    month = []
    order_pay = []
    order_pay1 = []
    year_rate = []
    for a, b, c, d, e in utils.get_rl_data():
        month.append(a[-2:] + '月')
        order_pay.append(round(b / 10000, 0))
        order_pay1.append(round(d / 10000, 0))
        year_rate.append(e)
        print(year_rate)
    return jsonify({'month': month, 'order_pay': order_pay, 'order_pay1': order_pay1, 'year_rate': year_rate})


@app.route('/l2')
def get_l2_data():
    res = []
    for tup in utils.get_l2_data():
        res.append({"value": int(tup[1]), "name": tup[0]})
    return jsonify({"data": res})


@app.route('/r2')
def get_r2_data():
    res = []
    for tup in utils.get_r2_data():
        res.append({'name': tup[0], 'value': int(tup[1])})
    return jsonify({'data': res})


if __name__ == '__main__':
    app.run(port=8080)
