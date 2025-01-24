% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/avgExpCalc.R
\name{avgExpCalc}
\alias{avgExpCalc}
\title{A avgExpCalc Function}
\usage{
avgExpCalc(dataObj, assay = "RNA", group.by)
}
\arguments{
\item{dataObj}{scRNA object with log-normalized data}

\item{assay}{Single cell data Assay type ("RNA", "SCT"). Default "RNA"}

\item{group.by}{Calculate average expression by given group}
}
\description{
This function allows you to calculate average gene expression on
long-normalized data by group defined by user
}
\examples{
##Input Expression data
#avgExpCalc(dataObj, group.by)
}
\keyword{avgExpCalc}
