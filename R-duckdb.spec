#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-duckdb
Version  : 1.1.1
Release  : 3
URL      : https://cran.r-project.org/src/contrib/duckdb_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/duckdb_1.1.1.tar.gz
Summary  : DBI Package for the DuckDB Database Management System
Group    : Development/Tools
License  : MIT
Requires: R-duckdb-lib = %{version}-%{release}
Requires: R-DBI
BuildRequires : R-DBI
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
system with support for the Structured Query Language (SQL). This
    package includes all of DuckDB and an R Database Interface (DBI)
    connector.

%package lib
Summary: lib components for the R-duckdb package.
Group: Libraries

%description lib
lib components for the R-duckdb package.


%prep
%setup -q -n duckdb

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729117426

%install
export SOURCE_DATE_EPOCH=1729117426
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/duckdb/DESCRIPTION
/usr/lib64/R/library/duckdb/INDEX
/usr/lib64/R/library/duckdb/LICENSE
/usr/lib64/R/library/duckdb/Meta/Rd.rds
/usr/lib64/R/library/duckdb/Meta/features.rds
/usr/lib64/R/library/duckdb/Meta/hsearch.rds
/usr/lib64/R/library/duckdb/Meta/links.rds
/usr/lib64/R/library/duckdb/Meta/nsInfo.rds
/usr/lib64/R/library/duckdb/Meta/package.rds
/usr/lib64/R/library/duckdb/NAMESPACE
/usr/lib64/R/library/duckdb/NEWS.md
/usr/lib64/R/library/duckdb/R/duckdb
/usr/lib64/R/library/duckdb/R/duckdb.rdb
/usr/lib64/R/library/duckdb/R/duckdb.rdx
/usr/lib64/R/library/duckdb/help/AnIndex
/usr/lib64/R/library/duckdb/help/aliases.rds
/usr/lib64/R/library/duckdb/help/duckdb.rdb
/usr/lib64/R/library/duckdb/help/duckdb.rdx
/usr/lib64/R/library/duckdb/help/figures/logo.png
/usr/lib64/R/library/duckdb/help/paths.rds
/usr/lib64/R/library/duckdb/html/00Index.html
/usr/lib64/R/library/duckdb/html/R.css
/usr/lib64/R/library/duckdb/icons/duckdb.png
/usr/lib64/R/library/duckdb/include/cpp11.hpp
/usr/lib64/R/library/duckdb/include/cpp11/R.hpp
/usr/lib64/R/library/duckdb/include/cpp11/altrep.hpp
/usr/lib64/R/library/duckdb/include/cpp11/as.hpp
/usr/lib64/R/library/duckdb/include/cpp11/attribute_proxy.hpp
/usr/lib64/R/library/duckdb/include/cpp11/data_frame.hpp
/usr/lib64/R/library/duckdb/include/cpp11/declarations.hpp
/usr/lib64/R/library/duckdb/include/cpp11/doubles.hpp
/usr/lib64/R/library/duckdb/include/cpp11/environment.hpp
/usr/lib64/R/library/duckdb/include/cpp11/external_pointer.hpp
/usr/lib64/R/library/duckdb/include/cpp11/function.hpp
/usr/lib64/R/library/duckdb/include/cpp11/integers.hpp
/usr/lib64/R/library/duckdb/include/cpp11/list.hpp
/usr/lib64/R/library/duckdb/include/cpp11/list_of.hpp
/usr/lib64/R/library/duckdb/include/cpp11/logicals.hpp
/usr/lib64/R/library/duckdb/include/cpp11/matrix.hpp
/usr/lib64/R/library/duckdb/include/cpp11/named_arg.hpp
/usr/lib64/R/library/duckdb/include/cpp11/protect.hpp
/usr/lib64/R/library/duckdb/include/cpp11/r_bool.hpp
/usr/lib64/R/library/duckdb/include/cpp11/r_string.hpp
/usr/lib64/R/library/duckdb/include/cpp11/r_vector.hpp
/usr/lib64/R/library/duckdb/include/cpp11/raws.hpp
/usr/lib64/R/library/duckdb/include/cpp11/sexp.hpp
/usr/lib64/R/library/duckdb/include/cpp11/strings.hpp
/usr/lib64/R/library/duckdb/include/duckdb_types.hpp
/usr/lib64/R/library/duckdb/libs/symbols.rds
/usr/lib64/R/library/duckdb/rstudio/connections.dcf
/usr/lib64/R/library/duckdb/rstudio/connections/DuckDB.R
/usr/lib64/R/library/duckdb/tests/testthat.R
/usr/lib64/R/library/duckdb/tests/testthat/_snaps/backend-dbplyr__duckdb_connection.md
/usr/lib64/R/library/duckdb/tests/testthat/_snaps/explain.md
/usr/lib64/R/library/duckdb/tests/testthat/_snaps/multi_statement.md
/usr/lib64/R/library/duckdb/tests/testthat/_snaps/types.md
/usr/lib64/R/library/duckdb/tests/testthat/data/binary_string.parquet
/usr/lib64/R/library/duckdb/tests/testthat/data/userdata1.parquet
/usr/lib64/R/library/duckdb/tests/testthat/helper-DBItest.R
/usr/lib64/R/library/duckdb/tests/testthat/helper-arrow.R
/usr/lib64/R/library/duckdb/tests/testthat/test-DBItest.R
/usr/lib64/R/library/duckdb/tests/testthat/test-adbc.R
/usr/lib64/R/library/duckdb/tests/testthat/test-ambiguous_prepare.R
/usr/lib64/R/library/duckdb/tests/testthat/test-arrow.R
/usr/lib64/R/library/duckdb/tests/testthat/test-arrow_stream.R
/usr/lib64/R/library/duckdb/tests/testthat/test-backend-dbplyr__duckdb_connection.R
/usr/lib64/R/library/duckdb/tests/testthat/test-bind.R
/usr/lib64/R/library/duckdb/tests/testthat/test-config_keyvalue.R
/usr/lib64/R/library/duckdb/tests/testthat/test-connect.R
/usr/lib64/R/library/duckdb/tests/testthat/test-dbQuoteIdentifier__duckdb_connection.R
/usr/lib64/R/library/duckdb/tests/testthat/test-dbinfo.R
/usr/lib64/R/library/duckdb/tests/testthat/test-dbwritetable.R
/usr/lib64/R/library/duckdb/tests/testthat/test-explain.R
/usr/lib64/R/library/duckdb/tests/testthat/test-extension_path.R
/usr/lib64/R/library/duckdb/tests/testthat/test-factor.R
/usr/lib64/R/library/duckdb/tests/testthat/test-fetch.R
/usr/lib64/R/library/duckdb/tests/testthat/test-fetch_arrow.R
/usr/lib64/R/library/duckdb/tests/testthat/test-integer64.R
/usr/lib64/R/library/duckdb/tests/testthat/test-interval.R
/usr/lib64/R/library/duckdb/tests/testthat/test-list.R
/usr/lib64/R/library/duckdb/tests/testthat/test-map.R
/usr/lib64/R/library/duckdb/tests/testthat/test-multi_statement.R
/usr/lib64/R/library/duckdb/tests/testthat/test-null_byte.R
/usr/lib64/R/library/duckdb/tests/testthat/test-parquet.R
/usr/lib64/R/library/duckdb/tests/testthat/test-read.R
/usr/lib64/R/library/duckdb/tests/testthat/test-readonly.R
/usr/lib64/R/library/duckdb/tests/testthat/test-register.R
/usr/lib64/R/library/duckdb/tests/testthat/test-register_arrow.R
/usr/lib64/R/library/duckdb/tests/testthat/test-register_readonly.R
/usr/lib64/R/library/duckdb/tests/testthat/test-rel_api.R
/usr/lib64/R/library/duckdb/tests/testthat/test-relational.R
/usr/lib64/R/library/duckdb/tests/testthat/test-rfuns.R
/usr/lib64/R/library/duckdb/tests/testthat/test-shutdown.R
/usr/lib64/R/library/duckdb/tests/testthat/test-struct.R
/usr/lib64/R/library/duckdb/tests/testthat/test-tbl__duckdb_connection.R
/usr/lib64/R/library/duckdb/tests/testthat/test-timestamp.R
/usr/lib64/R/library/duckdb/tests/testthat/test-timezone.R
/usr/lib64/R/library/duckdb/tests/testthat/test-types.R
/usr/lib64/R/library/duckdb/tests/testthat/test-viewer.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/duckdb/libs/duckdb.so
