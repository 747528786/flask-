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
    return jsonify({"sum_total": data_order[0], "per_store": data_order[1], "per_order": data_order[2], "new_store": data[0]})


@app.route('/m2')
def get_m2_data():
    res = []
    for tup in utils.get_map_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})


@app.route('/l1')
def get_l1_data():
    GT_sku = []
    GT_num = []
    KA_sku = []
    KA_num = []
    for s, n, k in utils.get_l1_data():
        if k == 1:
            GT_sku.append(str(s))
            GT_num.append(int(n))
        if k == 2:
            KA_sku.append(s)
            KA_num.append(int(n))
    return jsonify({'sku': ['AP3', 'AC3', 'AP2', 'AP1', 'NC3', 'NC Tin S3', 'AC4', 'AC2', 'AP4', 'AP1MINI'],
                    'data_GT': GT_num,
                    'data_KA': KA_num})


@app.route('/rl')
def get_rl_data():
    year = []
    amount = []
    for y, a in utils.get_rl_data():
        year.append(y)
        amount.append(a)
    return jsonify({'year': year, 'amount': amount})


@app.route('/l2')
def get_l2_data():
    res = []
    for tup in utils.get_l2_data():
        res.append({"value": int(tup[1]), "name": tup[0]})
    print(res)
    return jsonify({"data": res})


@app.route('/r2')
def get_r2_data():
    res = []
    for tup in utils.get_r2_data():
        res.append({'name': tup[0], 'value': int(tup[1])})
    return jsonify({'data': res})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
