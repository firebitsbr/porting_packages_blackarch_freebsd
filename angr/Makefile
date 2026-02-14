PORTNAME=	angr
DISTVERSION=	9.2.194
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The next-generation binary analysis platform from UC Santa Barbaras Seclab.
WWW=		https://pypi.org/project/angr/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-setuptools-rust@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/rust

RUN_DEPENDS=	??/libffi \
		??/py-ailment@${PY_FLAVOR} \
		??/py-ana@${PY_FLAVOR} \
		??/py-archinfo@${PY_FLAVOR} \
		??/py-bintrees@${PY_FLAVOR} \
		??/py-cachetools@${PY_FLAVOR} \
		??/py-capstone@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-claripy@${PY_FLAVOR} \
		??/py-cle@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-cooldict@${PY_FLAVOR} \
		??/py-cppheaderparser@${PY_FLAVOR} \
		??/py-cxxheaderparser@${PY_FLAVOR} \
		??/py-dpkt@${PY_FLAVOR} \
		??/py-gitpython@${PY_FLAVOR} \
		??/py-itanium-demangler@${PY_FLAVOR} \
		??/py-lmdb@${PY_FLAVOR} \
		??/py-msgspec@${PY_FLAVOR} \
		??/py-mulpyplexer@${PY_FLAVOR} \
		??/py-nampa@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-progressbar@${PY_FLAVOR} \
		??/py-protobuf@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pydemumble@${PY_FLAVOR} \
		??/py-pyelftools@${PY_FLAVOR} \
		??/py-pyformlang@${PY_FLAVOR} \
		??/py-pyvex@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-rpyc@${PY_FLAVOR} \
		??/py-simuvex@${PY_FLAVOR} \
		??/py-sortedcontainers@${PY_FLAVOR} \
		??/py-sympy@${PY_FLAVOR} \
		??/py-unicorn@${PY_FLAVOR} \
		??/py-unique-log-filter@${PY_FLAVOR} \
		??/py-z3-solver@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
