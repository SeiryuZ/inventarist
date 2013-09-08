import unicodecsv

from apps.products.models import Product


def generate_product_report(start_date, end_date):

    file_name = 'Laporan_Product-{start_date}-to-{end_date}.csv'.format(start_date=start_date, end_date=end_date)

    with open(file_name, 'wb') as csv_file:
        writer = unicodecsv.writer(csv_file, encoding='utf-8')
        header = ('Barang #ID', 'Nama Barang', 'Quantity')
        writer.writerow(header)

        for product in Product.objects.all():
            row = (product.id, product.name, product.quantity)
            writer.writerow(row)
