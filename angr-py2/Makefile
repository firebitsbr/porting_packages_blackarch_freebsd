PORTNAME=	angr-py2
DISTVERSION=	7.8.9.26
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The next-generation binary analysis platform from UC Santa Barbaras Seclab.
WWW=		https://pypi.org/project/angr/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

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
		??/py-cooldict@${PY_FLAVOR} \
		??/py-dpkt@${PY_FLAVOR} \
		??/py-gitpython@${PY_FLAVOR} \
		??/py-mulpyplexer@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-progressbar@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pyelftools@${PY_FLAVOR} \
		??/py-pyvex@${PY_FLAVOR} \
		??/py-rpyc@${PY_FLAVOR} \
		??/py-simuvex@${PY_FLAVOR} \
		??/py-sortedcontainers@${PY_FLAVOR} \
		??/py-unicorn@${PY_FLAVOR} \
		??/py-z3@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
