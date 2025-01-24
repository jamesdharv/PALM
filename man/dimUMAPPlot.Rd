% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/dimUMAPPlot.R
\name{dimUMAPPlot}
\alias{dimUMAPPlot}
\title{A dimUMAPPlot Function}
\usage{
dimUMAPPlot(
  ann,
  rnaObj = NULL,
  countMat = NULL,
  nPC = 30,
  gene_oi = NULL,
  groupName = NULL,
  plotname = NULL,
  filePATH = NULL,
  fileName = NULL
)
}
\arguments{
\item{ann}{Annotation table. Table must consist column Sample (Participant
sample name), PTID (Participant), Time (longitudinal time points), group,
name of the group, group_donor (combined string using group:Sample)}

\item{rnaObj}{The seurat scRNA object in case of single cell RNA data (optional).}

\item{countMat}{Expression matrix or data frame. Rows represents gene/proteins
column represents participant samples (same as annotation table Sample column),
in case count matrix for expression data (optional).}

\item{nPC}{Number of PCAs to be used for UMAP, Default is 30}

\item{gene_oi}{Genes of interest to explore, required}

\item{groupName}{User-defined group name column from annotation table or seurat
annotation column, required}

\item{plotname}{User-defined output file name, required}

\item{filePATH}{User-defined output directory PATH Default, current directory}

\item{fileName}{User-defined file name, Default outputFile}
}
\description{
This function allows you to perform UMAP visualization of gene of interest list.
}
\examples{
##Count/genescore matrix data
#dimUMAPPlot(ann=annotation, countMat=countData, nPC=15, gene_oi=var_gene, 
#groupName="celltype", plotname="variable", filePATH=filePATH, fileName="ATAC")

##Single cell RNA data
#dimUMAPPlot(rnaObj=SeuratObj, nPC=15, gene_oi=var_gene, groupName="celltype",
#plotname="variable", filePATH=filePATH, fileName="scRNA")
}
\keyword{dimUMAPPlot}
