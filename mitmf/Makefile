PORTNAME=	mitmf
DISTVERSION=	v0.9.8.r73.g0458300
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Framework for Man-In-The-Middle attacks written in Python.
WWW=		https://github.com/byt3bl33d3r/MITMf

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/backdoor-factory \
		??/capstone \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-configobj@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-msgpack@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-netfilterqueue@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pyinotify@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		??/py-user-agents@${PY_FLAVOR} \
		??/systemd \
		devel/py-setuptools@${PY_FLAVOR} \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
