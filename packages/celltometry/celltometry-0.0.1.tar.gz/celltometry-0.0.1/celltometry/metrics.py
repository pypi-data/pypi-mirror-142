import pandas as pd
import scanpy as sc

## Evaluation metrics

# Integration metrics

def compute_scib_metrics(AnnData, emb_key, label_key, batch_key, model_name):
    try:
        from scib.metrics.silhouette import silhouette_batch, silhouette
        from scib.metrics.lisi import lisi_graph
    except ImportError:
        return ((print("scib is required for using scib as scoring method."
                       " Please install it with `pip install scib`. ")))
    emb_key_ = "X_emb"
    AnnData.obsm[emb_key_] = AnnData.obsm[emb_key]
    sc.pp.neighbors(AnnData, use_rep=emb_key_)
    df = pd.DataFrame(index=[model_name])
    df["ilisi"], df["clisi"] = lisi_graph(AnnData, batch_key, label_key, type_="embed")
    df["sil_batch"] = silhouette_batch(AnnData, batch_key, label_key, emb_key_)
    df["sil_labels"] = silhouette(AnnData, label_key, emb_key_)
    return df

