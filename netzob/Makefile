PORTNAME=	netzob
DISTVERSION=	1.0.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An open source tool for reverse engineering, traffic generation and fuzzing of communication protocols.
WWW=		https://github.com/netzob/netzob/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/graphviz \
		??/gtk3 \
		??/impacket \
		??/libxml2 \
		??/py-arpreq@${PY_FLAVOR} \
		??/py-bintrees@${PY_FLAVOR} \
		??/py-bitarray@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-gobject@${PY_FLAVOR} \
		??/py-jsonpickle@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pcapy@${PY_FLAVOR} \
		??/py-pylstar@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		lang/python \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
