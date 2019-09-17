import numpy as np
import pandas as pd
import pathlib

def generate_edgelist(n_nodes, rel_ratio_min=0.1, rel_ratio_max=0.3, n_nodes_mu=4.5, weight_mu=2, weight_sigma=0.5):
    df_list = []
    for i in range(6):
        rel_min = int((n_nodes - 6) * rel_ratio_min)
        rel_max = int((n_nodes - 6) * rel_ratio_max)
        if rel_max <= 1:
            rel_max = 2
        n_suppliers = np.random.randint(rel_min, rel_max, 1)
        n_customers = np.random.randint(rel_min, rel_max, 1)
        suppliers = np.random.choice(list(range(6, n_nodes)), n_suppliers, replace=False)
        customers = np.random.choice(list(range(6, n_nodes)), n_customers, replace=False)
        supplier_weights = np.random.normal(weight_mu * (np.log(n_nodes) / n_nodes_mu), weight_sigma, n_suppliers)
        customer_weights = np.random.normal(weight_mu * (np.log(n_nodes) / n_nodes_mu), weight_sigma, n_customers)
        df_suppliers = pd.DataFrame({
            'src': i,
            'dst': suppliers,
            'weight': supplier_weights
        })
        df_customers = pd.DataFrame({
            'src': customers,
            'dst': i,
            'weight': customer_weights
        })
        df_list.append(df_suppliers)
        df_list.append(df_customers)
    df_edges = pd.concat(df_list)
    df_edges = df_edges[df_edges['weight'] > 0].reset_index(drop=True)
    return df_edges

def generate_files(output_dir, n_graphs=1000, n_nodes_mu=4.5, n_nodes_sigma=1.0):
    # make data directory
    path = pathlib.Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    # generate graphs
    n_nodes_list = np.random.lognormal(n_nodes_mu, n_nodes_sigma, n_graphs).astype(int) + 8
    for i in range(n_graphs):
        df_edgelist = generate_edgelist(n_nodes_list[i])
        while df_edgelist.empty:
            df_edgelist = generate_edgelist(n_nodes_list[i])
        filename = path / '{}.edgelist'.format(i)
        df_edgelist.to_csv(filename, header=False, index=False)
    # generate target file
    target_ratios = np.sqrt(6 / n_nodes_list)
    targets = [ np.random.choice([0, 1], p=[1-r, r]) for r in target_ratios ]
    df_targets = pd.DataFrame({
        'company_id': list(range(n_graphs)),
        'target': targets
    }).set_index('company_id')
    filename = path / 'target.csv'
    df_targets.to_csv(filename)

if __name__ == '__main__':
    np.random.seed(123)
    train_data_dir = 'data/train'
    test_data_dir = 'data/test'
    generate_files(train_data_dir)
    generate_files(test_data_dir)
