import numpy as np
import scanpy as sc
import scanpy.external as sce
from scipy.sparse import csr_matrix
from topo import TopOGraph

def preprocess(AnnData, target_sum=1e4, min_mean=0.0125, max_mean=8, min_disp=0.3, save_to_raw=True, plot_hvg=False):
    """
    A wrapper around Scanpy's preprocessing functions. Normalizes RNA library by size, logarithmizes it and
    selects highly variable genes for subsetting the AnnData object. Automatically subsets the Anndata
    object and saves the full expression matrix to AnnData.raw.


    Parameters
    ----------
    AnnData: the target AnnData object.

    target_sum: int (optional, default 1e4).
        constant for library size normalization.

    min_mean: float (optional, default 0.0125).
        Minimum gene expression level for inclusion as highly-variable gene.

    max_mean: float (optional, default 8.0).
        Maximum gene expression level for inclusion as highly-variable gene.

    min_disp: float (optional, default 0.3).
        Minimum expression dispersion for inclusion as highly-variable gene.

    save_to_raw: bool (optional, default True).
        Whether to save the full expression matrix to AnnData.raw.

    plot_hvg: bool (optional, default False)
        Whether to plot the high-variable genes plot.

    Returns
    -------

    Updated AnnData object.

    """
    sc.pp.normalize_total(AnnData, target_sum=target_sum)
    sc.pp.log1p(AnnData)
    sc.pp.highly_variable_genes(AnnData, min_mean=min_mean, max_mean=max_mean, min_disp=min_disp)
    if plot_hvg:
        sc.pl.highly_variable_genes(AnnData)
    if save_to_raw:
        AnnData.raw = AnnData
    AnnData = AnnData[:, AnnData.var.highly_variable]
    return AnnData





def default_workflow(AnnData, n_neighbors=15, n_pcs=50, metric='euclidean', scale=False,
                     resolution=0.8, min_dist=0.5, spread=1, maxiter=600):
    """

    A wrapper around scanpy's default workflow: mean-center and scale the data, perform PCA and use its
    output to construct k-Nearest-Neighbors graphs. These graphs are used for louvain clustering and
    laid out with UMAP. For simplicity, only the main arguments are included; we recommend you tailor
    a simple personalized workflow if you want to optimize hyperparameters.

    Parameters
    ----------

    AnnData: the target AnnData object.

    n_neighbors: int (optional, default 15).
        Number of neighbors for kNN graph construction.

    n_pcs: int (optional, default 50).
        Number of principal components to retain for downstream analysis.

    metric: str (optional, default 'euclidean').
        Metric used for neighborhood graph construction. Common values are 'euclidean' and 'cosine'.

    resolution: float (optional, default 0.8).
        Resolution parameter for the leiden graph community clustering algorithm.

    min_dist: float (optional, default 0.5).
        Key hyperparameter for UMAP embedding. Smaller values lead to more 'concentrated' graphs, however can
        lead to loss of global structure. Recommended values are between 0.3 and 0.8.

    spread: float (optional, default 1.0).
        Key hyperparameter for UMAP embedding. Controls the global spreading of data in the embedidng during
        optimization. Larger values lead to more spread out layouts, but can lead to loss of local structure.
        Ideally, this parameter should vary with `min_dist`.

    maxiter: int (optional, 600).
        Number of maximum iterations for the UMAP embedding optimization.


    Returns
    -------

    Updated AnnData object.

    """

    if not scale:
        adata_scale = AnnData
        sc.pp.scale(adata_scale, max_value=10)
        sc.tl.pca(adata_scale, n_comps=n_pcs)
        sc.pp.neighbors(adata_scale, n_neighbors=n_neighbors, metric=metric)
        sc.tl.leiden(adata_scale, resolution=resolution)
        sc.tl.umap(adata_scale, min_dist=min_dist, spread=spread, maxiter=maxiter)
        AnnData.obsm['X_pca'] = adata_scale.obsm['X_pca']
        AnnData.obsm['X_pca_umap'] = adata_scale.obsm['X_umap']
        AnnData.obs['pca_leiden'] = adata_scale.obs['leiden']
    else:
        sc.pp.scale(AnnData, max_value=10)
        sc.tl.pca(AnnData, n_comps=n_pcs)
        sc.pp.neighbors(AnnData, n_neighbors=n_neighbors, metric=metric)
        sc.tl.leiden(AnnData, resolution=resolution)
        sc.tl.umap(AnnData, min_dist=min_dist, spread=spread, maxiter=maxiter)
        AnnData.obsm['X_pca_umap'] = AnnData.obsm['X_umap']
        AnnData.obs['pca_leiden'] = AnnData.obs['leiden']
    return AnnData


def default_integration_workflow(AnnData,
                                 integration_method=['harmony', 'scanorama', 'bbknn'],
                                 batch_key='batch',
                                 n_neighbors=15,
                                 n_pcs=50,
                                 metric='euclidean',
                                 resolution=0.8,
                                 min_dist=0.5,
                                 spread=1,
                                 maxiter=600,
                                 **kwargs):
    """

    A wrapper around scanpy's default integration workflows: harmony, scanorama and bbknn.

    Parameters
    ----------

    AnnData: the target AnnData object.

    integration_method: str( optional, default ['harmony', 'scanorama', 'bbknn', 'scvi']).
        Which integration methods to run. Defaults to all.

    n_neighbors: int (optional, default 15).
        Number of neighbors for kNN graph construction.

    n_pcs: int (optional, default 50).
        Number of principal components to retain for downstream analysis in scanorama.

    metric: str (optional, default 'euclidean').
        Metric used for neighborhood graph construction. Common values are 'euclidean' and 'cosine'.

    resolution: float (optional, default 0.8).
        Resolution parameter for the leiden graph community clustering algorithm.

    min_dist: float (optional, default 0.5).
        Key hyperparameter for UMAP embedding. Smaller values lead to more 'concentrated' graphs, however can
        lead to loss of global structure. Recommended values are between 0.3 and 0.8.

    spread: float (optional, default 1.0).
        Key hyperparameter for UMAP embedding. Controls the global spreading of data in the embedidng during
        optimization. Larger values lead to more spread out layouts, but can lead to loss of local structure.
        Ideally, this parameter should vary with `min_dist`.

    maxiter: int (optional, 600).
        Number of maximum iterations for the UMAP embedding optimization.

    kwargs: additional parameters to be passed for the integration method. To use this option,
        select only one integration method at a time - otherwise, it'll raise several errors.


    Returns
    -------

    Batch-corrected and updated AnnData object.

    """
    # Batch-correct latent representations
    # With harmony

    if 'harmony' in integration_method:
        sce.pp.harmony_integrate(AnnData, key=batch_key, basis='X_pca',
                                 adjusted_basis='X_pca_harmony', **kwargs)
        sc.pp.neighbors(AnnData, use_rep='X_pca_harmony', n_neighbors=n_neighbors, metric=metric)
        sc.tl.leiden(AnnData, key_added='pca_harmony_leiden', resolution=resolution)
        sc.tl.umap(AnnData, min_dist=min_dist, maxiter=maxiter, spread=spread)
        AnnData.obsm['X_pca_harmony_umap'] = AnnData.obsm['X_umap']


    if 'scanorama' in integration_method:
        try:
            import scanorama
        except ImportError:
            return((print("scanorama is required for using scanorama as batch-correction method."
                          " Please install it with `pip install scanorama`. ")))

        # subset the individual dataset to the same variable genes as in MNN-correct.
        # split per batch into new objects.
        batches = AnnData.obs[batch_key].cat.categories.tolist()
        alldata = {}
        for batch in batches:
            alldata[batch] = AnnData[AnnData.obs[batch_key] == batch, ]

        # convert to list of AnnData objects
        adatas = list(alldata.values())
        # run scanorama.integrate
        scanorama.integrate_scanpy(adatas, dimred=n_pcs, **kwargs)
        # Get all the integrated matrices.
        scanorama_int = [ad.obsm['X_scanorama'] for ad in adatas]
        # make into one matrix.
        all_s = np.concatenate(scanorama_int)
        print(all_s.shape)
        # add to the AnnData object
        AnnData.obsm["X_pca_scanorama"] = all_s
        sc.pp.neighbors(AnnData, use_rep='X_pca_scanorama', n_neighbors=n_neighbors, metric=metric)
        sc.tl.leiden(AnnData, key_added='pca_scanorama_leiden', resolution=resolution)
        sc.tl.umap(AnnData, min_dist=min_dist, maxiter=maxiter, spread=spread)
        AnnData.obsm['X_pca_scanorama_umap'] = AnnData.obsm['X_umap']

    if 'bbknn' in integration_method:
        try:
            import bbknn
        except ImportError:
            return((print("bbknn is required for using BBKNN as batch-correction method."
                          " Please install it with `pip install bbknn`. ")))
        if 'pca_leiden' not in AnnData.obs.keys():
            sc.pp.neighbors(AnnData, n_neighbors=n_neighbors, metric=metric)
            sc.tl.leiden(AnnData, resolution=resolution, key_added='pca_leiden')
        bbknn.ridge_regression(AnnData, batch_key=batch_key, confounder_key=['pca_leiden'])
        bbknn.bbknn(AnnData, batch_key=batch_key, use_rep='X_pca',
                    n_pcs=None, **kwargs)
        bbknn_graph = csr_matrix(AnnData.obsp['connectivities'])
        sc.tl.leiden(AnnData, key_added='pca_BBKNN_leiden', adjacency=bbknn_graph, resolution=resolution)
        sc.tl.umap(AnnData, min_dist=min_dist, maxiter=maxiter, spread=spread)
        AnnData.obsm['X_pca_bbknn_umap'] = AnnData.obsm['X_umap']

    # if 'scvi' in integration_method:
    #     try:
    #         import scvi
    #     except ImportError:
    #         return((print("scvi is required for using scvi as batch-correction method."
    #                       " Please install it with `pip install scvi-tools`. ")))
    #     scvi.data.setup_anndata(AnnData, batch_key=batch_key)
    #     vae = scvi.model.SCVI(AnnData, n_layers=5, n_latent=n_pcs, gene_likelihood="nb")
    #     vae.train()
    #     AnnData.obsm["X_scVI"] = vae.get_latent_representation()
    #     sc.pp.neighbors(AnnData, use_rep='X_scvi', n_neighbors=n_neighbors, metric=metric)
    #     sc.tl.leiden(AnnData, key_added='scvi_leiden', resolution=resolution)
    #     sc.tl.umap(AnnData, min_dist=min_dist, maxiter=maxiter, spread=spread)
    #     AnnData.obsm['X_scvi_umap'] = AnnData.obsm['X_umap']

    return AnnData



def topological_workflow(AnnData, topograph=None,
                         bases=['diffusion', 'fuzzy'],
                         graphs=['diff', 'fuzzy'],
                         layouts=['MAP', 'PaCMAP', 'tSNE', 'NCVis', 'TriMAP', 'MDE'],
                         resolution=0.8,
                         X_to_csr=True, **kwargs):
    """

    A wrapper around TopOMetry's topological workflow. Certain topological metrics are used to build new
     orthogonal bases, which in turn are used to learn new topological graphs from latent topology. These bases
     and graphs can then be used by different layout algorithms to generate visualizations. Clustering is performed
     with the leiden algorithm on the topological graphs. This wrapper takes an AnnData object containing a
      cell per feature matrix (np.ndarray or scipy.sparse.csr_matrix) and a TopOGraph object. If no TopOGraph object is
       provided, it will generate a new one. The TopOGraph object keeps all similarity and adjacency matrices
     used in analyses, but all dimensional reduction and clustering results are added directly to the AnnData object.


     All parameters for the topological analysis must have been added to the TopOGraph object beforehand; otherwise,
     default parameters will be used. Within this wrapper, users only select which topological models and layout options
     they wish to run. For hyperparameter tuning, the embeddings must be obtained separetely.


    Parameters
    ----------

    AnnData: the target AnnData object.

    topograph: celltometry.TopOGraph (optional).
        The TopOGraph object containing parameters for the topological analysis.

    bases : str (optional, default ['diffusion', 'continuous','fuzzy']).
         Which bases to compute. Defaults to all. To run only one or two bases, set it to
         ['fuzzy', 'diffusion'] or ['continuous'], for exemple.

    graphs : str (optional, default ['diff', 'cknn','fuzzy'])
         Which graphs to compute. Defaults to all. To run only one or two graphs, set it to
         ['fuzzy', 'diff'] or ['cknn'], for exemple.

    layouts : str (optional, default all ['tSNE', 'MAP', 'MDE', 'PaCMAP', 'TriMAP', 'NCVis'])
         Which layouts to compute. Defaults to all 6 options within TopOMetry: tSNE, MAP, MDE, PaCMAP,
         TriMAP and NCVis. To run only one or two layouts, set it to
         ['tSNE', 'MAP'] or ['PaCMAP'], for exemple.

    resolution : float (optional, default 0.8).
        Resolution parameter for the leiden graph community clustering algorithm.

    X_to_csr : bool (optional, default True).
        Whether to convert the data matrix in AnnData.X to a csr_matrix format prior to analysis. This is quite
        useful if the data matrix is rather sparse and may significantly speed up computations.

    kwargs : dict (optional)
        Additional parameters to be passed to the sc.tl.leiden() function for clustering.

    Returns
    -------

    Updated AnnData object.

    """

    if topograph is None:
        topograph = TopOGraph()
    if X_to_csr:
        from scipy.sparse import csr_matrix
        data = csr_matrix(AnnData.X)
    topograph.run_layouts(data, bases=bases, graphs=graphs, layouts=layouts)
    # Add the TopOGraph orthogonal bases and layouts to AnnData.obsm
    if 'diffusion' in bases:
        AnnData.obsm['X_db'] = topograph.MSDiffMap
        if 'PaCMAP' in layouts:
            AnnData.obsm['X_db_PaCMAP'] = topograph.db_PaCMAP
        if 'tSNE' in layouts:
            AnnData.obsm['X_db_tSNE'] = topograph.db_tSNE
        if 'TriMAP' in layouts:
            AnnData.obsm['X_db_TriMAP'] = topograph.db_TriMAP
        if 'NCVis' in layouts:
            AnnData.obsm['X_db_NCVis'] = topograph.db_NCVis
        if 'MAP' in layouts:
            if 'diff' in graphs:
                AnnData.obsm['X_db_diff_MAP'] = topograph.db_diff_MAP
            if 'fuzzy' in graphs:
                AnnData.obsm['X_db_fuzzy_MAP'] = topograph.db_fuzzy_MAP
            if 'cknn' in graphs:
                AnnData.obsm['X_db_cknn_MAP'] = topograph.db_cknn_MAP
        if 'MDE' in layouts:
            if 'diff' in graphs:
                AnnData.obsm['X_db_diff_MDE'] = topograph.db_diff_MDE
            if 'fuzzy' in graphs:
                AnnData.obsm['X_db_fuzzy_MDE'] = topograph.db_fuzzy_MDE
            if 'cknn' in graphs:
                AnnData.obsm['X_db_cknn_MDE'] = topograph.db_cknn_MDE
        # clustering
        if 'diff' in graphs:
            if 'db_diff_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=topograph.db_diff_graph, resolution=resolution,
                             key_added='db_diff_leiden', **kwargs)
        if 'fuzzy' in graphs:
            if 'db_fuzzy_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=topograph.db_fuzzy_graph, resolution=resolution,
                             key_added='db_fuzzy_leiden', **kwargs)
        if 'cknn' in graphs:
            if 'db_cknn_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=topograph.db_cknn_graph, resolution=resolution,
                             key_added='db_cknn_leiden', **kwargs)

    if 'fuzzy' in bases:
        AnnData.obsm['X_fb'] = topograph.FuzzyLapMap
        if 'PaCMAP' in layouts:
            AnnData.obsm['X_fb_PaCMAP'] = topograph.fb_PaCMAP
        if 'tSNE' in layouts:
            AnnData.obsm['X_fb_tSNE'] = topograph.fb_tSNE
        if 'TriMAP' in layouts:
            AnnData.obsm['X_fb_TriMAP'] = topograph.fb_TriMAP
        if 'NCVis' in layouts:
            AnnData.obsm['X_fb_NCVis'] = topograph.fb_NCVis
        if 'MAP' in layouts:
            if 'diff' in graphs:
                AnnData.obsm['X_fb_diff_MAP'] = topograph.fb_diff_MAP
            if 'fuzzy' in graphs:
                AnnData.obsm['X_fb_fuzzy_MAP'] = topograph.fb_fuzzy_MAP
            if 'cknn' in graphs:
                AnnData.obsm['X_fb_cknn_MAP'] = topograph.fb_cknn_MAP
        if 'MDE' in layouts:
            if 'diff' in graphs:
                AnnData.obsm['X_fb_diff_MDE'] = topograph.fb_diff_MDE
            if 'fuzzy' in graphs:
                AnnData.obsm['X_fb_fuzzy_MDE'] = topograph.fb_fuzzy_MDE
            if 'cknn' in graphs:
                AnnData.obsm['X_fb_cknn_MDE'] = topograph.fb_cknn_MDE
        # clustering
        if 'diff' in graphs:
            if 'fb_diff_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=topograph.fb_diff_graph, resolution=resolution,
                             key_added='fb_diff_leiden', **kwargs)
        if 'fuzzy' in graphs:
            if 'fb_fuzzy_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=topograph.fb_fuzzy_graph, resolution=resolution,
                             key_added='fb_fuzzy_leiden', **kwargs)
        if 'cknn' in graphs:
            if 'fb_cknn_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=topograph.fb_cknn_graph, resolution=resolution,
                             key_added='fb_cknn_leiden', **kwargs)
    if 'continuous' in bases:
        AnnData.obsm['X_cb'] = topograph.CLapMap
        if 'PaCMAP' in layouts:
            AnnData.obsm['X_cb_PaCMAP'] = topograph.cb_PaCMAP
        if 'tSNE' in layouts:
            AnnData.obsm['X_cb_tSNE'] = topograph.cb_tSNE
        if 'TriMAP' in layouts:
            AnnData.obsm['X_cb_TriMAP'] = topograph.cb_TriMAP
        if 'NCVis' in layouts:
            AnnData.obsm['X_cb_NCVis'] = topograph.cb_NCVis
        if 'MAP' in layouts:
            if 'diff' in graphs:
                AnnData.obsm['X_cb_diff_MAP'] = topograph.cb_diff_MAP
            if 'fuzzy' in graphs:
                AnnData.obsm['X_cb_fuzzy_MAP'] = topograph.cb_fuzzy_MAP
            if 'cknn' in graphs:
                AnnData.obsm['X_cb_cknn_MAP'] = topograph.cb_cknn_MAP
        if 'MDE' in layouts:
            if 'diff' in graphs:
                AnnData.obsm['X_cb_diff_MDE'] = topograph.cb_diff_MDE
            if 'fuzzy' in graphs:
                AnnData.obsm['X_cb_fuzzy_MDE'] = topograph.cb_fuzzy_MDE
            if 'cknn' in graphs:
                AnnData.obsm['X_cb_cknn_MDE'] = topograph.cb_cknn_MDE
        # clustering
        if 'diff' in graphs:
            if 'cb_diff_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=topograph.cb_diff_graph, resolution=resolution,
                             key_added='cb_diff_leiden', **kwargs)
        if 'fuzzy' in graphs:
            if 'cb_fuzzy_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=topograph.cb_fuzzy_graph, resolution=resolution,
                             key_added='cb_fuzzy_leiden', **kwargs)
        if 'cknn' in graphs:
            if 'cb_cknn_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=topograph.cb_cknn_graph, resolution=resolution,
                             key_added='cb_cknn_leiden', **kwargs)

    return AnnData



def topological_harmony_integration(AnnData, topograph=None, batch_key='batch',
                                     bases=['diffusion', 'fuzzy'],
                                     graphs=['diff', 'fuzzy'],
                                     layouts=['MAP', 'PaCMAP'],
                                     resolution=0.8,
                                     X_to_csr=True,
                                     **kwargs):
    """

    A wrapper around TopOMetry's topological workflow using [Harmony](https://doi.org/10.1038/s41592-019-0619-0)
     for data integration.
    For each batch, certain topological metrics are used to build new
     orthogonal bases. These orthogonal bases are harmonized with Harmony, and then
      are used to learn new topological graphs from latent topology. These harmonized bases
     and graphs can then be used by different layout algorithms to generate visualizations. Clustering is performed
     with the leiden algorithm on the topological graphs. This wrapper takes an AnnData object containing a
      cell per feature matrix (np.ndarray or scipy.sparse.csr_matrix) and a TopOGraph object. If no TopOGraph object is
       provided, it will generate a new one. The TopOGraph object keeps all similarity and adjacency matrices
     used in analyses, but all dimensional reduction and clustering results are added directly to the AnnData object.


     All parameters for the topological analysis must have been added to the TopOGraph object beforehand; otherwise,
     default parameters will be used. Within this wrapper, users only select which topological models and layout options
     they wish to run. For hyperparameter tuning, the embeddings must be obtained separetely.


    Parameters
    ----------

    AnnData: the target AnnData object.

    topograph: celltometry.TopOGraph (optional).
        The TopOGraph object containing parameters for the topological analysis.

    batch_key: str (optional, default 'batch').
        Which key of AnnData.obs contains batch information for data integration.

    bases : str (optional, default ['diffusion', 'continuous','fuzzy']).
         Which bases to compute. Defaults to all. To run only one or two bases, set it to
         ['fuzzy', 'diffusion'] or ['continuous'], for exemple.

    graphs : str (optional, default ['diff', 'cknn','fuzzy'])
         Which graphs to compute. Defaults to all. To run only one or two graphs, set it to
         ['fuzzy', 'diff'] or ['cknn'], for exemple.

    layouts : str (optional, default all ['tSNE', 'MAP', 'MDE', 'PaCMAP', 'TriMAP', 'NCVis'])
         Which layouts to compute. Defaults to all 6 options within TopOMetry: tSNE, MAP, MDE, PaCMAP,
         TriMAP and NCVis. To run only one or two layouts, set it to
         ['tSNE', 'MAP'] or ['PaCMAP'], for exemple.

    resolution : float (optional, default 0.8).
        Resolution parameter for the leiden graph community clustering algorithm.

    X_to_csr : bool (optional, default True).
        Whether to convert the data matrix in AnnData.X to a csr_matrix format prior to analysis. This is quite
        useful if the data matrix is rather sparse and may significantly speed up computations.

    kwargs : dict (optional)
        Additional parameters to be passed to [harmonypy](https://github.com/slowkow/harmonypy).

    Returns
    -------

    Tuple containing the updated AnnData object and the TopOGraph object with harmonized bases.

    """

    if topograph is None:
        topograph = TopOGraph()

    batches = AnnData.obs[batch_key].cat.categories.tolist()
    alldata = []
    for batch in batches:
        alldata.append(AnnData[AnnData.obs[batch_key] == batch, ].copy())
    for adata in alldata:
        tg_new = TopOGraph(base_knn=topograph.base_knn,
                         graph_knn=topograph.graph_knn,
                         n_eigs=topograph.n_eigs,
                         basis=topograph.basis,
                         graph=topograph.graph,
                         base_metric=topograph.base_metric,
                         graph_metric=topograph.graph_metric,
                         n_jobs=topograph.n_jobs,
                         backend=topograph.backend,
                         M=topograph.M,
                         efC=topograph.efC,
                         efS=topograph.efS,
                         verbosity=topograph.verbosity,
                         cache_base=topograph.cache_base,
                         cache_graph=topograph.cache_graph,
                         kernel_use=topograph.kernel_use,
                         alpha=topograph.alpha,
                         plot_spectrum=topograph.plot_spectrum,
                         eigen_expansion=topograph.eigen_expansion,
                         delta=topograph.delta,
                         t=topograph.t,
                         p=topograph.p,
                         transitions=topograph.transitions,
                         random_state=topograph.random_state)
        adata = topological_workflow(adata, tg_new, bases=bases,
                                     graphs=graphs, layouts=layouts,
                                     resolution=resolution, X_to_csr=X_to_csr)

    latent_size_db = []
    latent_size_fb = []
    latent_size_cb = []

    for adata in alldata:
        if 'diffusion' in bases:
            latent_size_db.append(np.shape(adata.obsm['X_db'])[1])
        if 'fuzzy' in bases:
            latent_size_fb.append(np.shape(adata.obsm['X_fb'])[1])
        if 'continuous' in bases:
            latent_size_cb.append(np.shape(adata.obsm['X_cb'])[1])

    min_size_db = np.min(latent_size_db)
    min_size_fb = np.min(latent_size_fb)
    min_size_cb = np.min(latent_size_cb)

    for adata in alldata:
        if 'diffusion' in bases:
            adata.obsm['X_db'] = adata.obsm['X_db'][:, 0:min_size_db]
        if 'fuzzy' in bases:
            adata.obsm['X_fb'] = adata.obsm['X_fb'][:, 0:min_size_fb]
        if 'continuous' in bases:
            adata.obsm['X_cb'] = adata.obsm['X_cb'][:, 0:min_size_cb]

    AnnData = alldata[0].concatenate(alldata[1:], join='inner', batch_key=batch_key)


    # if not verbose:
    #     topograph.verbosity = 0
    # # Split per batch into new objects.
    # if X_to_csr:
    #     from scipy.sparse import csr_matrix
    #     data = csr_matrix(AnnData.X)
    # else:
    #     data = AnnData.X
    #     # Get latent representations
    # if 'diffusion' in bases:
    #     if topograph.MSDiffMap is None:
    #         topograph.basis = 'diffusion'
    #         topograph.fit(data)
    #     AnnData.obsm['X_db'] = topograph.MSDiffMap
    # if 'continuous' in bases:
    #     if topograph.CLapMap is None:
    #         topograph.basis = 'continuous'
    #         topograph.fit(data)
    #     AnnData.obsm['X_cb'] = topograph.CLapMap
    # if 'fuzzy' in bases:
    #     if topograph.FuzzyLapMap is None:
    #         topograph.basis = 'fuzzy'
    #         topograph.fit(data)
    #     AnnData.obsm['X_fb'] = topograph.FuzzyLapMap

    # Batch-correct latent representations
    TopOGraph_harmony = topograph
    if TopOGraph_harmony.random_state is None:
        TopOGraph_harmony.random_state = np.random.RandomState()
    if 'diffusion' in bases:
        sce.pp.harmony_integrate(AnnData, key=batch_key, basis='X_db',
                                 adjusted_basis='X_db_harmony', **kwargs)
        TopOGraph_harmony.MSDiffMap = AnnData.obsm['X_db_harmony']
        if 'diff' in graphs:
            TopOGraph_harmony.graph = 'diff'
            db_harmony_diff_graph = TopOGraph_harmony.transform()
        if 'cknn' in graphs:
            topograph.graph = 'cknn'
            db_harmony_cknn_graph = TopOGraph_harmony.transform()
        if 'fuzzy' in graphs:
            topograph.graph = 'fuzzy'
            db_harmony_fuzzy_graph = TopOGraph_harmony.transform()
    if 'fuzzy' in bases:
        sce.pp.harmony_integrate(AnnData, key=batch_key, basis='X_fb',
                                 adjusted_basis='X_fb_harmony', **kwargs)
        TopOGraph_harmony.FuzzyLapMap = AnnData.obsm['X_fb_harmony']
        if 'diff' in graphs:
            TopOGraph_harmony.graph = 'diff'
            fb_harmony_diff_graph = TopOGraph_harmony.transform()
        if 'cknn' in graphs:
            TopOGraph_harmony.graph = 'cknn'
            fb_harmony_cknn_graph = TopOGraph_harmony.transform()
        if 'fuzzy' in graphs:
            TopOGraph_harmony.graph = 'fuzzy'
            fb_harmony_fuzzy_graph = TopOGraph_harmony.transform()
    if 'continuous' in bases:
        sce.pp.harmony_integrate(AnnData, key=batch_key, basis='X_cb',
                                 adjusted_basis='X_cb_harmony', **kwargs)
        TopOGraph_harmony.CLapMap = AnnData.obsm['X_fb_harmony']
        if 'diff' in graphs:
            TopOGraph_harmony.graph = 'diff'
            cb_harmony_diff_graph = TopOGraph_harmony.transform()
        if 'cknn' in graphs:
            TopOGraph_harmony.graph = 'cknn'
            cb_harmony_cknn_graph = TopOGraph_harmony.transform()
        if 'fuzzy' in graphs:
            TopOGraph_harmony.graph = 'fuzzy'
            cb_harmony_fuzzy_graph = TopOGraph_harmony.transform()
    # Run layouts
    if X_to_csr:
        from scipy.sparse import csr_matrix
        data = csr_matrix(AnnData.X)
    else:
        data = AnnData.X

    TopOGraph_harmony.run_layouts(data, bases=bases, graphs=graphs, layouts=layouts)
    # Add to adata and cluster with leiden
    if 'diffusion' in bases:
        if 'PaCMAP' in layouts:
            AnnData.obsm['db_harmony_PaCMAP'] = TopOGraph_harmony.db_PaCMAP
        if 'tSNE' in layouts:
            AnnData.obsm['db_harmony_tSNE'] = TopOGraph_harmony.db_tSNE
        if 'TriMAP' in layouts:
            AnnData.obsm['db_harmony_TriMAP'] = TopOGraph_harmony.db_TriMAP
        if 'diff' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['db_harmony_diff_MAP'] = TopOGraph_harmony.db_diff_MAP
            if 'MDE' in layouts:
                AnnData.obsm['db_harmony_diff_MDE'] = TopOGraph_harmony.db_diff_MDE
            if 'db_harmony_diff_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_harmony.db_diff_graph, resolution=resolution,
                             key_added='db_harmony_diff_leiden')
        if 'cknn' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['db_harmony_cknn_MAP'] = TopOGraph_harmony.db_cknn_MAP
            if 'MDE' in layouts:
                AnnData.obsm['db_harmony_cknn_MDE'] = TopOGraph_harmony.db_cknn_MDE
            if 'db_harmony_fuzzy_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_harmony.db_fuzzy_graph, resolution=resolution,
                             key_added='db_harmony_fuzzy_leiden')
        if 'fuzzy' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['db_harmony_fuzzy_MAP'] = TopOGraph_harmony.db_fuzzy_MAP
            if 'MDE' in layouts:
                AnnData.obsm['db_harmony_fuzzy_MDE'] = TopOGraph_harmony.db_fuzzy_MDE
            if 'db_harmony_cknn_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_harmony.db_cknn_graph, resolution=resolution,
                             key_added='db_harmony_cknn_leiden')
    if 'fuzzy' in bases:
        if 'PaCMAP' in layouts:
            AnnData.obsm['fb_harmony_PaCMAP'] = TopOGraph_harmony.fb_PaCMAP
        if 'tSNE' in layouts:
            AnnData.obsm['fb_harmony_tSNE'] = TopOGraph_harmony.fb_tSNE
        if 'TriMAP' in layouts:
            AnnData.obsm['fb_harmony_TriMAP'] = TopOGraph_harmony.fb_TriMAP
        if 'diff' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['fb_harmony_diff_MAP'] = TopOGraph_harmony.fb_diff_MAP
            if 'MDE' in layouts:
                AnnData.obsm['fb_harmony_diff_MDE'] = TopOGraph_harmony.fb_diff_MDE
            if 'fb_harmony_diff_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_harmony.fb_diff_graph, resolution=resolution,
                             key_added='fb_harmony_diff_leiden')
        if 'cknn' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['fb_harmony_cknn_MAP'] = TopOGraph_harmony.fb_cknn_MAP
            if 'MDE' in layouts:
                AnnData.obsm['fb_harmony_cknn_MDE'] = TopOGraph_harmony.fb_cknn_MDE
            if 'fb_harmony_cknn_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_harmony.fb_cknn_graph, resolution=resolution,
                             key_added='fb_harmony_cknn_leiden')
        if 'fuzzy' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['fb_harmony_fuzzy_MAP'] = TopOGraph_harmony.fb_fuzzy_MAP
            if 'MDE' in layouts:
                AnnData.obsm['fb_harmony_fuzzy_MDE'] = TopOGraph_harmony.fb_fuzzy_MDE
            if 'fb_harmony_fuzzy_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_harmony.fb_fuzzy_graph, resolution=resolution,
                             key_added='fb_harmony_fuzzy_leiden')
    if 'continuous' in bases:
        if 'PaCMAP' in layouts:
            AnnData.obsm['cb_harmony_PaCMAP'] = TopOGraph_harmony.fb_PaCMAP
        if 'tSNE' in layouts:
            AnnData.obsm['cb_harmony_tSNE'] = TopOGraph_harmony.fb_tSNE
        if 'TriMAP' in layouts:
            AnnData.obsm['cb_harmony_TriMAP'] = TopOGraph_harmony.fb_TriMAP
        if 'diff' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['cb_harmony_diff_MAP'] = TopOGraph_harmony.cb_diff_MAP
            if 'MDE' in layouts:
                AnnData.obsm['cb_harmony_diff_MDE'] = TopOGraph_harmony.cb_diff_MDE
            if 'cb_harmony_diff_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_harmony.cb_diff_graph, resolution=resolution,
                             key_added='cb_harmony_diff_leiden')
        if 'cknn' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['cb_harmony_cknn_MAP'] = TopOGraph_harmony.cb_cknn_MAP
            if 'MDE' in layouts:
                AnnData.obsm['cb_harmony_cknn_MDE'] = TopOGraph_harmony.cb_cknn_MDE
            if 'cb_harmony_cknn_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_harmony.cb_cknn_graph, resolution=resolution,
                             key_added='cb_harmony_cknn_leiden')
        if 'fuzzy' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['cb_harmony_fuzzy_MAP'] = TopOGraph_harmony.cb_fuzzy_MAP
            if 'MDE' in layouts:
                AnnData.obsm['cb_harmony_fuzzy_MDE'] = TopOGraph_harmony.cb_fuzzy_MDE
            if 'cb_harmony_fuzzy_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_harmony.cb_fuzzy_graph, resolution=resolution,
                             key_added='cb_harmony_fuzzy_leiden')

    return AnnData, TopOGraph_harmony


def topological_scanorama_integration(AnnData, TopOGraph, batch_key='batch',
                                      bases=['diffusion', 'fuzzy'],
                                      graphs=['diff', 'fuzzy'],
                                      layouts=['MAP', 'PaCMAP'],
                                      resolution=0.8,
                                      X_to_csr=True,
                                      **kwargs):
    """

    A wrapper around TopOMetry's topological workflow using [scanorama](https://doi.org/10.1038/s41587-019-0113-3)
    for data integration. For each batch, certain topological metrics are used to build new
    orthogonal bases. These orthogonal bases are harmonized with Scanorama, and then
    are used to learn new topological graphs from latent topology. These harmonized bases
    and graphs can then be used by different layout algorithms to generate visualizations. Clustering is performed
    with the leiden algorithm on the topological graphs. This wrapper takes an AnnData object containing a
    cell per feature matrix (np.ndarray or scipy.sparse.csr_matrix) and a TopOGraph object. If no TopOGraph object is
    provided, it will generate a new one. The TopOGraph object keeps all similarity and adjacency matrices
    used in analyses, but all dimensional reduction and clustering results are added directly to the AnnData object.

     All parameters for the topological analysis must have been added to the TopOGraph object beforehand; otherwise,
     default parameters will be used. Within this wrapper, users only select which topological models and layout options
     they wish to run. For hyperparameter tuning, the embeddings must be obtained separetely.


    Parameters
    ----------

    AnnData: the target AnnData object.

    topograph: celltometry.TopOGraph (optional).
        The TopOGraph object containing parameters for the topological analysis.

    batch_key: str (optional, default 'batch').
        Which key of AnnData.obs contains batch information for data integration.

    bases : str (optional, default ['diffusion', 'continuous','fuzzy']).
         Which bases to compute. Defaults to all. To run only one or two bases, set it to
         ['fuzzy', 'diffusion'] or ['continuous'], for exemple.

    graphs : str (optional, default ['diff', 'cknn','fuzzy'])
         Which graphs to compute. Defaults to all. To run only one or two graphs, set it to
         ['fuzzy', 'diff'] or ['cknn'], for exemple.

    layouts : str (optional, default all ['tSNE', 'MAP', 'MDE', 'PaCMAP', 'TriMAP', 'NCVis'])
         Which layouts to compute. Defaults to all 6 options within TopOMetry: tSNE, MAP, MDE, PaCMAP,
         TriMAP and NCVis. To run only one or two layouts, set it to
         ['tSNE', 'MAP'] or ['PaCMAP'], for exemple.

    resolution : float (optional, default 0.8).
        Resolution parameter for the leiden graph community clustering algorithm.

    X_to_csr : bool (optional, default True).
        Whether to convert the data matrix in AnnData.X to a csr_matrix format prior to analysis. This is quite
        useful if the data matrix is rather sparse and may significantly speed up computations.

    kwargs : dict (optional)
        Additional parameters to be passed to [scanorama](https://github.com/brianhie/scanorama).

    Returns
    -------

    Tuple containing the updated AnnData object and the TopOGraph object with harmonized bases.

    """


    if X_to_csr:
        from scipy.sparse import csr_matrix
        data = csr_matrix(AnnData.X)
    else:
        data = csr_matrix(AnnData.X)
    TopOGraph.run_models(data, bases=bases, graphs=None)
    TopOGraph_scanorama = TopOGraph
    if 'diffusion' in bases:
        sce.pp.scanorama_integrate(AnnData, key=batch_key, basis='X_db',
                                   adjusted_basis='X_db_scanorama', **kwargs)
        TopOGraph_scanorama.MSDiffMap = AnnData.obsm['X_db_scanorama']
        if 'diff' in graphs:
            TopOGraph_scanorama.graph = 'diff'
            db_scanorama_diff_graph = TopOGraph_scanorama.transform()
        if 'cknn' in graphs:
            TopOGraph_scanorama.graph = 'cknn'
            db_scanorama_cknn_graph = TopOGraph_scanorama.transform()
        if 'fuzzy' in graphs:
            TopOGraph_scanorama.graph = 'fuzzy'
            db_scanorama_fuzzy_graph = TopOGraph_scanorama.transform()
    if 'fuzzy' in bases:
        sce.pp.scanorama_integrate(AnnData, key=batch_key, basis='X_fb',
                                   adjusted_basis='X_fb_scanorama', **kwargs)
        TopOGraph_scanorama.MSDiffMap = AnnData.obsm['X_fb_scanorama']
        if 'diff' in graphs:
            TopOGraph_scanorama.graph = 'diff'
            fb_scanorama_diff_graph = TopOGraph_scanorama.transform()
        if 'cknn' in graphs:
            TopOGraph_scanorama.graph = 'cknn'
            fb_scanorama_cknn_graph = TopOGraph_scanorama.transform()
        if 'fuzzy' in graphs:
            TopOGraph_scanorama.graph = 'fuzzy'
            fb_scanorama_fuzzy_graph = TopOGraph_scanorama.transform()
    if 'continuous' in bases:
        sce.pp.scanorama_integrate(AnnData, key=batch_key, basis='X_cb',
                                   adjusted_basis='X_cb_scanorama', **kwargs)
        TopOGraph_scanorama.MSDiffMap = AnnData.obsm['X_cb_scanorama']
        if 'diff' in graphs:
            TopOGraph_scanorama.graph = 'diff'
            cb_scanorama_diff_graph = TopOGraph_scanorama.transform()
        if 'cknn' in graphs:
            TopOGraph_scanorama.graph = 'cknn'
            cb_scanorama_cknn_graph = TopOGraph_scanorama.transform()
        if 'fuzzy' in graphs:
            TopOGraph_scanorama.graph = 'fuzzy'
            cb_scanorama_fuzzy_graph = TopOGraph_scanorama.transform()
    # Run layouts
    TopOGraph_scanorama.run_layouts(bases=bases, graphs=graphs, layouts=layouts)
    # Add to adata and cluster with leiden
    if 'diffusion' in bases:
        if 'PaCMAP' in layouts:
            AnnData.obsm['db_scanorama_PaCMAP'] = TopOGraph_scanorama.db_PaCMAP
        if 'tSNE' in layouts:
            AnnData.obsm['db_scanorama_tSNE'] = TopOGraph_scanorama.db_tSNE
        if 'TriMAP' in layouts:
            AnnData.obsm['db_scanorama_TriMAP'] = TopOGraph_scanorama.db_TriMAP
        if 'diff' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['db_scanorama_diff_MAP'] = TopOGraph_scanorama.db_diff_MAP
            if 'MDE' in layouts:
                AnnData.obsm['db_scanorama_diff_MDE'] = TopOGraph_scanorama.db_diff_MDE
            if 'db_scanorama_diff_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_scanorama.db_diff_graph, resolution=resolution,
                             key_added='db_scanorama_diff_leiden')
        if 'cknn' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['db_scanorama_cknn_MAP'] = TopOGraph_scanorama.db_cknn_MAP
            if 'MDE' in layouts:
                AnnData.obsm['db_scanorama_cknn_MDE'] = TopOGraph_scanorama.db_cknn_MDE
            if 'db_scanorama_fuzzy_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_scanorama.db_fuzzy_graph, resolution=resolution,
                             key_added='db_scanorama_fuzzy_leiden')
        if 'fuzzy' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['db_scanorama_fuzzy_MAP'] = TopOGraph_scanorama.db_fuzzy_MAP
            if 'MDE' in layouts:
                AnnData.obsm['db_scanorama_fuzzy_MDE'] = TopOGraph_scanorama.db_fuzzy_MDE
            if 'db_scanorama_cknn_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_scanorama.db_cknn_graph, resolution=resolution,
                             key_added='db_scanorama_cknn_leiden')

    if 'fuzzy' in bases:
        if 'PaCMAP' in layouts:
            AnnData.obsm['fb_scanorama_PaCMAP'] = TopOGraph_scanorama.fb_PaCMAP
        if 'tSNE' in layouts:
            AnnData.obsm['fb_scanorama_tSNE'] = TopOGraph_scanorama.fb_tSNE
        if 'TriMAP' in layouts:
            AnnData.obsm['fb_scanorama_TriMAP'] = TopOGraph_scanorama.fb_TriMAP
        if 'diff' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['fb_scanorama_diff_MAP'] = TopOGraph_scanorama.fb_diff_MAP
            if 'MDE' in layouts:
                AnnData.obsm['fb_scanorama_diff_MDE'] = TopOGraph_scanorama.fb_diff_MDE
            if 'fb_scanorama_diff_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_scanorama.fb_diff_graph, resolution=resolution,
                             key_added='fb_scanorama_diff_leiden')
        if 'cknn' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['fb_scanorama_cknn_MAP'] = TopOGraph_scanorama.fb_cknn_MAP
            if 'MDE' in layouts:
                AnnData.obsm['fb_scanorama_cknn_MDE'] = TopOGraph_scanorama.fb_cknn_MDE
            if 'fb_scanorama_cknn_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_scanorama.fb_cknn_graph, resolution=resolution,
                             key_added='fb_scanorama_cknn_leiden')
        if 'fuzzy' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['fb_scanorama_fuzzy_MAP'] = TopOGraph_scanorama.fb_fuzzy_MAP
            if 'MDE' in layouts:
                AnnData.obsm['fb_scanorama_fuzzy_MDE'] = TopOGraph_scanorama.fb_fuzzy_MDE
            if 'fb_scanorama_fuzzy_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_scanorama.fb_fuzzy_graph, resolution=resolution,
                             key_added='fb_scanorama_fuzzy_leiden')

    if 'continuous' in bases:
        if 'PaCMAP' in layouts:
            AnnData.obsm['cb_scanorama_PaCMAP'] = TopOGraph_scanorama.fb_PaCMAP
        if 'tSNE' in layouts:
            AnnData.obsm['cb_scanorama_tSNE'] = TopOGraph_scanorama.fb_tSNE
        if 'TriMAP' in layouts:
            AnnData.obsm['cb_scanorama_TriMAP'] = TopOGraph_scanorama.fb_TriMAP
        if 'diff' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['cb_scanorama_diff_MAP'] = TopOGraph_scanorama.cb_diff_MAP
            if 'MDE' in layouts:
                AnnData.obsm['cb_scanorama_diff_MDE'] = TopOGraph_scanorama.cb_diff_MDE
            if 'cb_scanorama_diff_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_scanorama.cb_diff_graph, resolution=resolution,
                             key_added='cb_scanorama_diff_leiden')
        if 'cknn' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['cb_scanorama_cknn_MAP'] = TopOGraph_scanorama.cb_cknn_MAP
            if 'MDE' in layouts:
                AnnData.obsm['cb_scanorama_cknn_MDE'] = TopOGraph_scanorama.cb_cknn_MDE
            if 'fb_scanorama_cknn_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_scanorama.cb_cknn_graph, resolution=resolution,
                             key_added='fb_scanorama_cknn_leiden')
        if 'fuzzy' in graphs:
            if 'MAP' in layouts:
                AnnData.obsm['cb_scanorama_fuzzy_MAP'] = TopOGraph_scanorama.cb_fuzzy_MAP
            if 'MDE' in layouts:
                AnnData.obsm['cb_scanorama_fuzzy_MDE'] = TopOGraph_scanorama.cb_fuzzy_MDE
            if 'cb_scanorama_fuzzy_leiden' not in AnnData.obs.keys():
                sc.tl.leiden(AnnData, adjacency=TopOGraph_scanorama.cb_fuzzy_graph, resolution=resolution,
                             key_added='cb_scanorama_fuzzy_leiden')
    return AnnData, TopOGraph_scanorama


def topological_bbknn_integration(AnnData, TopOGraph, batch_key='batch',
                                  bases=['diffusion', 'fuzzy'],
                                  layouts=['MAP', 'PaCMAP'],
                                  resolution=0.8,
                                  X_to_csr=True,
                                  **kwargs):
    """

    A wrapper around TopOMetry's topological workflow using [BBKNN](https://doi.org/10.1093/bioinformatics/btz625)
    for data integration.
    For each batch, certain topological metrics are used to build new
    orthogonal bases. Batch-balanced affinity graphs are then learned from these bases with BBKNN, and can be
    used to obtain different visualizations and clustering results. As of now, this only works with MAP and MDE
    for visualization. This wrapper takes an AnnData object containing a
    cell per feature matrix (np.ndarray or scipy.sparse.csr_matrix) and a TopOGraph object. If no TopOGraph object is
    provided, it will generate a new one. The TopOGraph object keeps all similarity and adjacency matrices
    used in analyses, but all dimensional reduction and clustering results are added directly to the AnnData object.


    All parameters for the topological analysis must have been added to the TopOGraph object beforehand; otherwise,
    default parameters will be used. Within this wrapper, users only select which topological models and layout options
    they wish to run. For hyperparameter tuning, the embeddings must be obtained separetely.


    Parameters
    ----------

    AnnData: the target AnnData object.

    topograph: celltometry.TopOGraph (optional).
        The TopOGraph object containing parameters for the topological analysis.

    batch_key: str (optional, default 'batch').
        Which key of AnnData.obs contains batch information for data integration.

    bases : str (optional, default ['diffusion', 'continuous','fuzzy']).
         Which bases to compute. Defaults to all. To run only one or two bases, set it to
         ['fuzzy', 'diffusion'] or ['continuous'], for exemple.

    graphs : str (optional, default ['diff', 'cknn','fuzzy'])
         Which graphs to compute. Defaults to all. To run only one or two graphs, set it to
         ['fuzzy', 'diff'] or ['cknn'], for exemple.

    layouts : str (optional, default all ['tSNE', 'MAP', 'MDE', 'PaCMAP', 'TriMAP', 'NCVis'])
         Which layouts to compute. Defaults to all 6 options within TopOMetry: tSNE, MAP, MDE, PaCMAP,
         TriMAP and NCVis. To run only one or two layouts, set it to
         ['tSNE', 'MAP'] or ['PaCMAP'], for exemple.

    resolution : float (optional, default 0.8).
        Resolution parameter for the leiden graph community clustering algorithm.

    X_to_csr : bool (optional, default True).
        Whether to convert the data matrix in AnnData.X to a csr_matrix format prior to analysis. This is quite
        useful if the data matrix is rather sparse and may significantly speed up computations.

    kwargs : dict (optional)
        Additional parameters to be passed to [BBKNN](https://github.com/Teichlab/bbknn).

    Returns
    -------

    Tuple containing the updated AnnData object and the TopOGraph object with harmonized bases.

    """

    try:
        import bbknn
    except ImportError:
        return((print("bbknn is required for using BBKNN as batch-correction method."
                      " Please install it with `pip install bbknn`. ")))

    # Now, adapting BBKNN is a little tricky. BBKNN returns a fuzzy weighted similarity graph,
    # but scanorama and harmony return a corrected latent representation. We'll use
    # TopOMetry topological models to build one or more similarity graph from this corrected basis.
    # For layout, however, BBKNN corrected similarities will have to be used either with a new uncorrected basis
    # we build with TopOMetry
    # or with the uncorrected basis of each batch, separately analyzed. For batch-correction purposes,
    # I went with the former option, so the BBKNN option may take a while more to run than scanorama and harmony.
    # This gives us a lot of algorithmic options to explore, but only MAP as layout option.
    #
    # Build new representation, if already not computed
    if X_to_csr:
        from scipy.sparse import csr_matrix
        data = csr_matrix(AnnData.X)
    else:
        data = csr_matrix(AnnData.X)

    TopOGraph.run_models(data, bases=bases, graphs=None)
    # This is a silly trick as it will rewrite the graph slots of a new TopOGraph object
    # and use slightly more memory, but will do for now #FIXME
    TopOGraph_bbknn = TopOGraph

    if 'diffusion' in bases:
        AnnData.obsm['X_db_uncorrected'] = TopOGraph_bbknn.MSDiffMap
        sc.pp.neighbors(AnnData, metric=TopOGraph.graph_metric, n_neighbors=TopOGraph.graph_knn,
                        use_rep='X_db_uncorrected')
        if 'db_leiden' not in AnnData.obs.keys():
            sc.tl.leiden(AnnData, key_added='db_leiden', resolution=resolution)
        bbknn.ridge_regression(AnnData, batch_key=batch_key, confounder_key=['db_leiden'])
        bbknn.bbknn(AnnData, batch_key=batch_key, use_rep='X_db_uncorrected', metric=TopOGraph.graph_metric,
                    n_pcs=None, *kwargs)
        db_bbknn_graph = csr_matrix(AnnData.obsp['connectivities'])
        if 'db_BBKNN_leiden' not in AnnData.obs.keys():
            sc.tl.leiden(AnnData, key_added='db_BBKNN_leiden', adjacency=db_bbknn_graph, resolution=resolution)
        TopOGraph_bbknn.db_bbknn_graph = db_bbknn_graph
        if 'MAP' in layouts:
            AnnData.obsm['X_db_BBKNN_MAP'] = TopOGraph_bbknn.MAP(graph=TopOGraph_bbknn.db_bbknn_graph,
                                                                 n_components=2)

    if 'fuzzy' in bases:
        AnnData.obsm['X_fb_uncorrected'] = TopOGraph_bbknn.FuzzyLapMap
        sc.pp.neighbors(AnnData, metric=TopOGraph.graph_metric, n_neighbors=TopOGraph.graph_knn,
                        use_rep='X_fb_uncorrected')
        sc.tl.leiden(AnnData, key_added='fb_leiden', resolution=resolution)
        bbknn.ridge_regression(AnnData, batch_key=batch_key, confounder_key=['fb_leiden'])
        bbknn.bbknn(AnnData, batch_key=batch_key, use_rep='X_fb_uncorrected', metric=TopOGraph.graph_metric,
                    n_pcs=None, **kwargs)
        fb_bbknn_graph = csr_matrix(AnnData.obsp['connectivities'])
        sc.tl.leiden(AnnData, key_added='fb_BBKNN_leiden', adjacency=fb_bbknn_graph, resolution=resolution)
        TopOGraph_bbknn.fb_bbknn_graph = fb_bbknn_graph
        if 'MAP' in layouts:
            AnnData.obsm['X_fb_BBKNN_MAP'] = TopOGraph_bbknn.MAP(graph=TopOGraph.fb_bbknn_graph)

    if 'continuous' in bases:
        AnnData.obsm['X_cb_uncorrected'] = TopOGraph_bbknn.CLapMap
        sc.pp.neighbors(AnnData, metric=TopOGraph.graph_metric, n_neighbors=TopOGraph.graph_knn,
                        use_rep='X_cb_uncorrected')
        sc.tl.leiden(AnnData, key_added='cb_leiden', resolution=resolution)
        bbknn.ridge_regression(AnnData, batch_key=batch_key, confounder_key=['cb_leiden'])
        bbknn.bbknn(AnnData, batch_key=batch_key, use_rep='X_cb_uncorrected', metric=TopOGraph.graph_metric,
                    n_pcs=None, **kwargs)
        cb_bbknn_graph = csr_matrix(AnnData.obsp['connectivities'])
        sc.tl.leiden(AnnData, key_added='cb_BBKNN_leiden', adjacency=cb_bbknn_graph, resolution=resolution)
        TopOGraph_bbknn.cb_bbknn_graph = cb_bbknn_graph
        if 'MAP' in layouts:
            AnnData.obsm['X_cb_BBKNN_MAP'] = TopOGraph_bbknn.MAP(graph=TopOGraph.cb_bbknn_graph)

    return AnnData, TopOGraph_bbknn

