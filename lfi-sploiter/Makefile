PORTNAME=	lfi-sploiter
DISTVERSION=	1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	This tool helps you exploit LFI (Local File Inclusion) vulnerabilities. Post discovery, simply pass the affected URL and vulnerable parameter to this tool. You can also use this tool to scan a URL for LFI vulnerabilities.
WWW=		http://packetstormsecurity.com/files/96056/Simple-Local-File-Inclusion-Exploiter-1.0.html

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/py-httplib2@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
