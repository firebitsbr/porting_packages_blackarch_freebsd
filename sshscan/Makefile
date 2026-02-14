PORTNAME=	sshscan
DISTVERSION=	1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A horizontal SSH scanner that scans large swaths of IPv4 space for a single SSH user and pass.
WWW=		https://github.com/getdual/scripts-n-tools/blob/master/sshscan.py

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-netaddr@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
