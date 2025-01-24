% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/StableFeatures.R
\name{StableFeatures}
\alias{StableFeatures}
\title{A StableFeatures Function}
\usage{
StableFeatures(
  ann = NULL,
  group_oi = NULL,
  meanThreshold = NULL,
  cvThreshold = NULL,
  donorThreshold = NULL,
  groupThreshold = NULL,
  topFeatures = 25,
  housekeeping_genes = NULL,
  filePATH = NULL,
  fileName = NULL
)
}
\arguments{
\item{ann}{Annotation table. Table must consist column Sample (Participant
sample name), PTID (Participant), Time (longitudinal time points)}

\item{group_oi}{Group of interest to focus on, Default is NULL}

\item{meanThreshold}{Average expression threshold to filter lowly expressed
genes Default is 0.1 (log2 scale)}

\item{cvThreshold}{Coefficient of variation threshold to select variable and
stable genes Default is 10 for single cell RNA (100*SD/mean)}

\item{donorThreshold}{Donor threshold number to be used, Default is number of
participants}

\item{groupThreshold}{Group label threshold number to be used, Default is
(number of participants x group labels)/2}

\item{topFeatures}{Number of features to be selected from each group, Default
is 25}

\item{housekeeping_genes}{Optional list of housekeeping genes to focus on.
Default is ACTB, GAPDH}

\item{filePATH}{User-defined output directory path to load the CV result obtained
from cvCalcSC function}

\item{fileName}{User defined filename}
}
\description{
This function allows you to identify stable genes in a participant across
longitudinal timepoints in single cell dataset. The coefficient of variation
(CV) obtained from 'cvCalcSC' function used to filter genes/features by CV
threshold (cvThreshold). User can identify cvThreshold in different datasets
using housekeeping genes CV distribution. The minimum expression of gene
(meanThreshold) used to remove lowly expressed genes (spike CV).
}
\examples{
##Single cell RNA data
#stablegene <- StableFeatures(ann=metadata, meanThreshold=0.1, cvThreshold=10,
#donorThreshold=donorThreshold, groupThreshold=groupThreshold,
#topFeatures=25, fileName="scRNA", filePATH=filePATH)
}
\keyword{StableFeatures}
