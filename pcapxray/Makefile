PORTNAME=	pcapxray
DISTVERSION=	3.0.r5.g1721645
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Network Forensics Tool - To visualize a Packet Capture offline as a Network Diagram including device identification, highlight important communication and file extraction.
WWW=		https://github.com/Srinivas11789/PcapXray

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-cryptography@${PY_FLAVOR} \
		??/py-graphviz@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pyshark@${PY_FLAVOR} \
		??/py-pyvis@${PY_FLAVOR} \
		??/py-stem@${PY_FLAVOR} \
		??/scapy \
		??/tk \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
